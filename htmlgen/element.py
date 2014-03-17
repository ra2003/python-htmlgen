try:
    from html import escape
except ImportError:
    from cgi import escape

from htmlgen.generator import Generator, HTMLChildGenerator


def html_attribute(attribute_name, default=None):
    """Add an attribute to an HTML element.

        >>> class MyElement(Element):
        ...     url = html_attribute("data-url")
        >>> element = MyElement("div")
        >>> element.url
        >>> str(element)
        '<div></div>'
        >>> element.url = "http://www.example.com/"
        >>> str(element)
        '<div data-url="http://www.example.com/"></div>'

    If the optional default argument is given, the attribute will not be
    included if the value matches it.

        >>> class MyElement(Element):
        ...     value = html_attribute("data-value", default="hello")
        >>> element = MyElement("div")
        >>> element.value
        'hello'
        >>> str(element)
        '<div></div>'

    """

    def get(self):
        return self.get_attribute(attribute_name, default=default)

    def set_(self, value):
        if value is None or value == default:
            self.remove_attribute(attribute_name)
        else:
            self.set_attribute(attribute_name, value)

    return property(get, set_)


def boolean_html_attribute(attribute_name):
    """Add a boolean attribute to an HTML element.

        >>> class MyElement(Element):
        ...     doit = boolean_html_attribute("data-doit")
        >>> element = MyElement("div")
        >>> element.doit
        False
        >>> str(element)
        '<div></div>'
        >>> element.doit = True
        >>> str(element)
        '<div data-doit="data-doit"></div>'

    """

    def get(self):
        return self.get_attribute(attribute_name) == attribute_name

    def set_(self, value):
        if value:
            self.set_attribute(attribute_name, attribute_name)
        else:
            self.remove_attribute(attribute_name)

    return property(get, set_)


def int_html_attribute(attribute_name, default=None):
    """Add an attribute to an HTML element that accepts only integers

        >>> class MyElement(Element):
        ...     value = int_html_attribute("data-value")
        >>> element = MyElement("div")
        >>> element.value
        >>> str(element)
        '<div></div>'
        >>> element.value = 42
        >>> str(element)
        '<div data-value="42"></div>'

    If the optional default argument is given, the attribute will not be
    included if the value matches it.

        >>> class MyElement(Element):
        ...     value = int_html_attribute("data-value", default=0)
        >>> element = MyElement("div")
        >>> element.value
        0
        >>> str(element)
        '<div></div>'

    """

    def get(self):
        value = self.get_attribute(attribute_name, default=default)
        if value is None:
            return None
        return int(value)

    def set_(self, value):
        if value is None or value == default:
            self.remove_attribute(attribute_name)
        else:
            self.set_attribute(attribute_name, str(value))

    return property(get, set_)


class _ElementBase(Generator):

    def __init__(self, element_name):
        super(_ElementBase, self).__init__()
        self.element_name = element_name
        self._attributes = {}
        self._css_classes = set()
        self._styles = {}

    def set_attribute(self, name, value):
        """Set a HTML attribute to a given string value.

            >>> element = Element("div")
            >>> element.set_attribute("title", "Test Title")
            >>> str(element)
            '<div title="Test Title"></div>'

        """
        self._attributes[name] = value

    def get_attribute(self, name, default=None):
        """Return the value of an HTML attribute.

        If the attribute is not set, return the default value.

        """
        return self._attributes.get(name, default)

    def remove_attribute(self, name):
        """Remove an HTML attribute from this element.

        If the attribute is not set, do nothing.

        """
        try:
            del self._attributes[name]
        except KeyError:
            pass

    def add_css_classes(self, *css_classes):
        """Add CSS classes to this element.

            >>> element = Element("div")
            >>> element.add_css_classes("my-css")
            >>> str(element)
            '<div class="my-css"></div>'

        """
        for cls in css_classes:
            self._css_classes.add(cls)

    def set_style(self, name, value):
        """Set a CSS style on this element.

            >>> element = Element("div")
            >>> element.set_style("background-color", "green")
            >>> str(element)
            '<div style="background-color: green"></div>'

        """
        self._styles[name] = value

    id = html_attribute("id")

    def render_start_tag(self):
        html = "<" + self.element_name
        for attribute, value in self._attributes.items():
            html += self._get_attribute_string(attribute, value)
        if self._css_classes:
            html += self._get_attribute_string("class", self._class_value)
        if self._styles:
            html += self._get_attribute_string("style", self._style_value)
        return html

    @staticmethod
    def _get_attribute_string(attribute, value):
        escaped_value = escape(value, True)
        return " " + attribute + '="' + escaped_value + '"'

    @property
    def _class_value(self):
        return " ".join(self._css_classes)

    @property
    def _style_value(self):
        rendered_styles = [name + ": " + value
                           for name, value in self._styles.items()]
        return "; ".join(rendered_styles)


class Element(_ElementBase):

    """Base generator for HTML elements with children.

    This includes most elements, like <body>, <div>, <span>, <strong>, etc.

        >>> link = Element("a")
        >>> link.set_attribute("href", "http://www.example.com/")
        >>> link.append("Test Link")
        >>> str(link)
        '<a href="http://www.example.com/">Test Link</a>'

    append() and extend() escape reserved HTML characters in string, but
    not in sub-generators:

        >>> span = Element("span")
        >>> span.add_css_classes("my-css")
        >>> span.set_style("color", "red")
        >>> span.append("Test & Test")
        >>> str(span)
        '<span class="my-css" style="color: red">Test &amp; Test</span>'

    append_raw() and extend_raw() do not do any escaping. Do not use these
    methods with strings from untrusted sources!

        >>> span = Element("span")
        >>> span.append_raw("Test<br/>Test")
        >>> str(span)
        '<span>Test<br/>Test</span>'

    Instead of appending children to elements, the generate_children()
    method can be overwritten. This is generally preferred for element
    sub-classes that are not meant to be extended by users, since it avoids
    constructing the HTML tree in memory.

        >>> class MyElement(Element):
        ...     def generate_children(self):
        ...         yield "Hello, "
        ...         child = Element("strong")
        ...         child.append("World!")
        ...         yield child
        >>> str(MyElement("div"))
        '<div>Hello, <strong>World!</strong></div>'

    """

    def __init__(self, element_name):
        super(Element, self).__init__(element_name)
        self.children = HTMLChildGenerator()

    def __bool__(self):
        return True

    def __getattr__(self, item):
        return getattr(self.children, item)

    def __len__(self):
        """Return the number of children.

        A sub-generator is counted as one child.

        """
        return len(self.children)

    def __nonzero__(self):
        return True

    def generate(self):
        yield self.render_start_tag() + ">"
        for element in self.generate_children():
            yield element
        yield "</" + self.element_name + ">"

    def generate_children(self):
        """Return an iterator over the children of this element.

        This method can be overwritten by sub-classes.

        """
        return self.children


class ShortElement(_ElementBase):

    """Base generator for content-less HTML elements.

    These are elements like <br> or <link>.

        >>> link = ShortElement("link")
        >>> link.set_attribute("rel", "stylesheet")
        >>> str(link)
        '<link rel="stylesheet"/>'

    """

    def generate(self):
        yield self.render_start_tag() + "/>"

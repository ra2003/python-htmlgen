def html_attribute(attribute_name, default=None):
    """Add an attribute to an HTML element.

        >>> from htmlgen import Element
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

        >>> from htmlgen import Element
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
    """Add an attribute to an HTML element that accepts only integers.

        >>> from htmlgen import Element
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


def float_html_attribute(attribute_name, default=None):
    """Add an attribute to an HTML element that accepts only numbers.

        >>> from htmlgen import Element
        >>> class MyElement(Element):
        ...     value = float_html_attribute("data-value")
        >>> element = MyElement("div")
        >>> element.value
        >>> str(element)
        '<div></div>'
        >>> element.value = 4.2
        >>> str(element)
        '<div data-value="4.2"></div>'

    If the optional default argument is given, the attribute will not be
    included if the value matches it.

        >>> class MyElement(Element):
        ...     value = float_html_attribute("data-value", default=0.4)
        >>> element = MyElement("div")
        >>> element.value
        0.4
        >>> str(element)
        '<div></div>'

    """

    def get(self):
        value = self.get_attribute(attribute_name, default=default)
        if value is None:
            return None
        return float(value)

    def set_(self, value):
        if value is None or value == default:
            self.remove_attribute(attribute_name)
        else:
            self.set_attribute(attribute_name, str(value))

    return property(get, set_)

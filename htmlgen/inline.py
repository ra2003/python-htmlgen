from htmlgen.element import Element


class Span(Element):

    """An HTML in-line <span> element.

    <span> elements are inline elements without semantic meaning. They are
    containers for styling or scripting.


        >>> span1 = Span("Example text")
        >>> span2 = Span()
        >>> span2.append("Example text")

    """

    def __init__(self, content=None):
        super(Span, self).__init__("span")
        if content:
            self.append(content)


class Highlight(Element):

    """An HTML in-line highlighting (<b>) element.

    <b> elements are used to highlight words or sentences, without giving
    more importance to them.

    Note: Despite the name, <b> elements are not necessarily displayed in a
    bold font. Use CSS for styling purposes.

    Compare with the Strong, Alternate, and Emphasis elements.

    Example:

        >>> span = Span()
        >>> span.append("The ")
        >>> span.append(Highlight("swordfish"))
        >>> span.append(" is a member of the ")
        >>> span.append(Alternate("Xiphiidae"))
        >>> span.append(" family.")

    """

    def __init__(self, content=None):
        super(Highlight, self).__init__("b")
        if content:
            self.append(content)


class Strong(Element):

    """An HTML in-line element for strong importance or urgency (<strong>).

    Compare with the Highlight, Alternate, and Emphasis elements.

    Example:

        >>> Strong("It is imperative to turn off the froblunator after use!"))

    """

    def __init__(self, content=None):
        super(Strong, self).__init__("strong")
        if content:
            self.append(content)


class Alternate(Element):

    """An HTML in-line element for alternate voice text (<i>).

    This includes the introduction of a term or thoughts.

    Note: Despite the name, <i> elements are not necessarily displayed in a
    italic font. Use CSS for styling purposes.

    Compare with the Highlight, Strong, and Emphasis elements.

    Example:

        >>> span = Span()
        >>> span.append("This is called a ")
        >>> span.append(Alternate("froblunator"))
        >>> span.append(".")

    """

    def __init__(self, content=None):
        super(Alternate, self).__init__("i")
        if content:
            self.append(content)


class Emphasis(Element):

    """An HTML stress emphasis (<em>) element.

    Compare with the Highlight, Strong, and Alternate elements.

    Example:

        >>> span = Span()
        >>> span.append(Emphasis("This"))
        >>> span.append(" is great.")

    """

    def __init__(self, content=None):
        super(Emphasis, self).__init__("em")
        if content:
            self.append(content)


class Small(Element):

    """An HTML in-line element for side comments and small print (<small>).

    Note: Text inside <small> elements is not necessarily rendered with a
    smaller font size than surrounding text. Use CSS for styling purposes.

    Example:

        >>> Small("Copyright (C) 2010")

    """

    def __init__(self, content=None):
        super(Small, self).__init__("small")
        if content:
            self.append(content)


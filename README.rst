Python HTML 5 Generator
=======================

*This library is currently in development. The API is subject to change.
Feedback and suggestions are welcome!*

Basic usage:

>>> from htmlgen import Division, Span
>>> div = Division()
>>> div.id = "my-block"
>>> div.append("This is ")
>>> span = Span()
>>> span.add_css_classes("important")
>>> span.append("important!")
>>> div.append(span)

A tree constructed like this can either be converted to a string:

>>> str(div)
'<div id="my-block">This is <span class="important">important!</span></div>'

Alternatively, all elements can be used as iterator, for example to return
them from a WSGI callback:

>>> def application(env, start_response):
...     start_response("200 OK", [("Content-Type", "text/html")])
...     return div

There are two different ways to render children of HTML elements. The tree
construction approach shown above is mainly suitable for elements with few
children. The disadvantage of this approach is that the whole tree must be
constructed in memory. An alternative way, best suited for custom sub-classes
of elements, is to override the generate_children method of the Element class:

>>> class MyBlock(Division):
...     def __init__(self):
...         super(MyBlock, self).__init__()
...         self.id = "my-block"
...     def generate_children(self):
...         yield "This is "
...         span = Span()
...         span.add_css_classes("important")
...         span.append("important!")
...         yield span
>>> str(MyBlock())
'<div id="my-block">This is <span class="important">important!</span></div>'

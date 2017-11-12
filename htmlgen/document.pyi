from typing import Any, Optional, Union, AnyStr

from htmlgen.element import Element, NonVoidElement, VoidElement
from htmlgen.generator import Generator

MIME_JAVASCRIPT: str = ...
MIME_JSON: str = ...

class Document(Generator):
    root: HTMLRoot = ...
    title: str = ...
    def __init__(self, title: Optional[str] = ..., language: str = ...) -> None: ...
    def add_stylesheets(self, *stylesheets: str) -> None: ...
    def add_stylesheet(self, stylesheet: str) -> None: ...
    def add_scripts(self, *scripts: str) -> None: ...
    def add_script(self, script: str) -> None: ...
    def append_head(self, child: Union[AnyStr, Generator]) -> None: ...
    def append_body(self, child: Union[AnyStr, Generator]) -> None: ...

class HTMLRoot(NonVoidElement):
    head: Head = ...
    body: Body = ...
    def __init__(self, title: Optional[str] = ..., language: str = ...) -> None: ...

class Head(Element):
    title: Title = ...
    def __init__(self, title: Optional[str] = ...) -> None: ...
    def add_stylesheets(self, *stylesheets: str) -> None: ...
    def add_stylesheet(self, stylesheet: str) -> None: ...
    def add_scripts(self, *scripts: str) -> None: ...
    def add_script(self, script: str) -> None: ...

class Body(Element):
    def __init__(self) -> None: ...

class Title(NonVoidElement):
    title: str = ...
    def __init__(self, title: Optional[str] = ...) -> None: ...

class Meta(VoidElement):
    def __init__(self) -> None: ...
    @classmethod
    def create_charset(cls, charset: str) -> "Meta": ...

class Script(NonVoidElement):
    url: Optional[str] = ...
    script: Optional[str] = ...
    type: str = ...
    def __init__(self, url: Optional[str] = ..., script: Optional[str] = ...) -> None: ...

def json_script(json: Any) -> Script: ...

class HeadLink(VoidElement):
    relation: str = ...
    url: str = ...
    def __init__(self, relation: str, url: str) -> None: ...
    @classmethod
    def create_stylesheet(cls, stylesheet: str) -> "HeadLink": ...

class Main(Element):
    def __init__(self) -> None: ...

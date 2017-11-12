import collections
import typing
from typing import \
    Any, AnyStr, Mapping, MutableMapping, Union, TypeVar, Set, Optional

from htmlgen.generator import Generator, HTMLChildGenerator

T = TypeVar("T")

def is_element(o: Any, element_name: str) -> bool: ...

class _ElementDataProxy(MutableMapping[str, str]):
    def __init__(self, element: _ElementBase) -> None: ...
    def clear(self) -> None: ...
    @classmethod
    def from_data(cls, element: _ElementBase, data: Mapping[str, str]) -> _ElementDataProxy: ...

class _ElementBase(Generator):
    id: Optional[str] = ...
    element_name: str = ...

    @property
    def data(self) -> _ElementDataProxy: ...
    @data.setter
    def data(self, data: Mapping[str, str]) -> None: ...

    def __init__(self, element_name: str) -> None: ...
    def set_attribute(self, name: str, value: str) -> None: ...
    def get_attribute(self, name: str, default: T = ...) -> Union[str, T]: ...
    def remove_attribute(self, name: str) -> None: ...
    @property
    def attribute_names(self) -> Set[str]: ...
    def add_css_classes(self, *css_classes: str) -> None: ...
    def remove_css_classes(self, *css_classes: str) -> None: ...
    def has_css_class(self, css_class: str) -> bool: ...
    def set_style(self, name: str, value: str) -> None: ...
    def render_start_tag(self) -> str: ...

class NonVoidElement(_ElementBase):
    def generate_children(self) -> typing.Generator[Union[AnyStr, Generator], None, None]: ...

class Element(NonVoidElement, collections.Sized):
    children: HTMLChildGenerator = ...
    def __init__(self, element_name: str) -> None: ...
    def __bool__(self) -> bool: ...
    def __getattr__(self, item: Any) -> Any: ...
    def __len__(self) -> int: ...
    def __nonzero__(self) -> bool: ...

class VoidElement(_ElementBase): ...

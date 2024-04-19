# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_message import Message
from ..types.enums.enm_category import Category
from ..types.partial.classes.cls_message import PartialMessage
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, List, Protocol, runtime_checkable


IClassifyConversationOutput = List[Category]

@runtime_checkable
class IClassifyConversation(Protocol):
    """
    This is the interface for a function.

    Args:
        messages: List[Message]

    Returns:
        List[Category]
    """

    async def __call__(self, *, messages: List[Message]) -> List[Category]:
        ...

   

@runtime_checkable
class IClassifyConversationStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        messages: List[Message]

    Returns:
        AsyncStream[List[Category], List[Category]]
    """

    def __call__(self, *, messages: List[Message]
) -> AsyncStream[List[Category], List[Category]]:
        ...
class IBAMLClassifyConversation(BaseBAMLFunction[List[Category], List[Category]]):
    def __init__(self) -> None:
        super().__init__(
            "ClassifyConversation",
            IClassifyConversation,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> List[Category]:
        return await self.get_impl("default_config").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[List[Category], List[Category]]:
        res = self.get_impl("default_config").stream(*args, **kwargs)
        return res

BAMLClassifyConversation = IBAMLClassifyConversation()

__all__ = [ "BAMLClassifyConversation" ]
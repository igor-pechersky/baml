# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_conversation import Conversation
from ..types.classes.cls_message import Message
from ..types.enums.enm_messagesender import MessageSender
from ..types.partial.classes.cls_conversation import PartialConversation
from ..types.partial.classes.cls_message import PartialMessage
from baml_core.stream import AsyncStream
from typing import Callable, Optional, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IMessageSimplifierOutput = Optional[int]

@runtime_checkable
class IMessageSimplifier(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: Conversation

    Returns:
        Optional[int]
    """

    async def __call__(self, arg: Conversation, /) -> Optional[int]:
        ...

   

@runtime_checkable
class IMessageSimplifierStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: Conversation

    Returns:
        AsyncStream[Optional[int], int]
    """

    def __call__(self, arg: Conversation, /) -> AsyncStream[Optional[int], int]:
        ...
class BAMLMessageSimplifierImpl:
    async def run(self, arg: Conversation, /) -> Optional[int]:
        ...
    
    def stream(self, arg: Conversation, /) -> AsyncStream[Optional[int], int]:
        ...

class IBAMLMessageSimplifier:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IMessageSimplifier, IMessageSimplifierStream], None]:
        ...

    async def __call__(self, arg: Conversation, /) -> Optional[int]:
        ...

    def stream(self, arg: Conversation, /) -> AsyncStream[Optional[int], int]:
        ...

    def get_impl(self, name: ImplName) -> BAMLMessageSimplifierImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the MessageSimplifierInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.MessageSimplifier.mock() as mocked:
                    mocked.return_value = ...
                    result = await MessageSimplifierImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MessageSimplifierInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.MessageSimplifier.test
            async def test_logic(MessageSimplifierImpl: IMessageSimplifier) -> None:
                result = await MessageSimplifierImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MessageSimplifierInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.MessageSimplifier.test(exclude_impl=["implname"])
            async def test_logic(MessageSimplifierImpl: IMessageSimplifier) -> None:
                result = await MessageSimplifierImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.MessageSimplifier.test(stream=True)
            async def test_logic(MessageSimplifierImpl: IMessageSimplifierStream) -> None:
                async for result in MessageSimplifierImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the MessageSimplifierInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.MessageSimplifier.test
        class TestClass:
            def test_a(self, MessageSimplifierImpl: IMessageSimplifier) -> None:
                ...
            def test_b(self, MessageSimplifierImpl: IMessageSimplifier) -> None:
                ...
        ```
        """
        ...

BAMLMessageSimplifier: IBAMLMessageSimplifier

# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_linteroutput import LinterOutput
from ..types.partial.classes.cls_linteroutput import PartialLinterOutput
from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["version1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IExampleProviderOutput = List[LinterOutput]

@runtime_checkable
class IExampleProvider(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        List[LinterOutput]
    """

    async def __call__(self, arg: str, /) -> List[LinterOutput]:
        ...

   

@runtime_checkable
class IExampleProviderStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[List[LinterOutput], List[LinterOutput]]
    """

    def __call__(self, arg: str, /) -> AsyncStream[List[LinterOutput], List[LinterOutput]]:
        ...
class BAMLExampleProviderImpl:
    async def run(self, arg: str, /) -> List[LinterOutput]:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[List[LinterOutput], List[LinterOutput]]:
        ...

class IBAMLExampleProvider:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IExampleProvider, IExampleProviderStream], None]:
        ...

    async def __call__(self, arg: str, /) -> List[LinterOutput]:
        ...

    def stream(self, arg: str, /) -> AsyncStream[List[LinterOutput], List[LinterOutput]]:
        ...

    def get_impl(self, name: ImplName) -> BAMLExampleProviderImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the ExampleProviderInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.ExampleProvider.mock() as mocked:
                    mocked.return_value = ...
                    result = await ExampleProviderImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExampleProviderInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.ExampleProvider.test
            async def test_logic(ExampleProviderImpl: IExampleProvider) -> None:
                result = await ExampleProviderImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExampleProviderInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.ExampleProvider.test(exclude_impl=["implname"])
            async def test_logic(ExampleProviderImpl: IExampleProvider) -> None:
                result = await ExampleProviderImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.ExampleProvider.test(stream=True)
            async def test_logic(ExampleProviderImpl: IExampleProviderStream) -> None:
                async for result in ExampleProviderImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExampleProviderInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.ExampleProvider.test
        class TestClass:
            def test_a(self, ExampleProviderImpl: IExampleProvider) -> None:
                ...
            def test_b(self, ExampleProviderImpl: IExampleProvider) -> None:
                ...
        ```
        """
        ...

BAMLExampleProvider: IBAMLExampleProvider
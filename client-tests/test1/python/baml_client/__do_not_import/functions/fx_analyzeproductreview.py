# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_reviewanalysis import ReviewAnalysis
from ..types.enums.enm_reviewhelpfulness import ReviewHelpfulness
from ..types.enums.enm_reviewsentiment import ReviewSentiment
from ..types.partial.classes.cls_reviewanalysis import PartialReviewAnalysis
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IAnalyzeProductReviewOutput = ReviewAnalysis

@runtime_checkable
class IAnalyzeProductReview(Protocol):
    """
    This is the interface for a function.

    Args:
        product_review: str

    Returns:
        ReviewAnalysis
    """

    async def __call__(self, *, product_review: str) -> ReviewAnalysis:
        ...

   

@runtime_checkable
class IAnalyzeProductReviewStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        product_review: str

    Returns:
        AsyncStream[ReviewAnalysis, PartialReviewAnalysis]
    """

    def __call__(self, *, product_review: str
) -> AsyncStream[ReviewAnalysis, PartialReviewAnalysis]:
        ...
class IBAMLAnalyzeProductReview(BaseBAMLFunction[ReviewAnalysis, PartialReviewAnalysis]):
    def __init__(self) -> None:
        super().__init__(
            "AnalyzeProductReview",
            IAnalyzeProductReview,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> ReviewAnalysis:
        return await self.get_impl("").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[ReviewAnalysis, PartialReviewAnalysis]:
        res = self.get_impl("").stream(*args, **kwargs)
        return res

BAMLAnalyzeProductReview = IBAMLAnalyzeProductReview()

__all__ = [ "BAMLAnalyzeProductReview" ]
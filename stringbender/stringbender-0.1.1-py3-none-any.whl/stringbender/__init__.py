from __future__ import annotations

import re
import sys
from typing import Callable, Iterable, List, Mapping, Sequence, Tuple, Union

DEFAULT_DELIMITERS: List[str] = [" ", ".", "-", "_", ":", "\\"]


def camel(s: str,
          delimiters: List[str] = DEFAULT_DELIMITERS,
          split_on_first_upper: bool = False) -> String:
    return String(s).camel(delimiters, split_on_first_upper)


def kebob(s: str,
          delimiters: List[str] = DEFAULT_DELIMITERS,
          split_on_first_upper: bool = False,
          title_case: bool = False) -> String:
    return String(s).kebob(delimiters, split_on_first_upper, title_case)


def pascal(s: str,
           delimiters: List[str] = DEFAULT_DELIMITERS,
           split_on_first_upper: bool = False) -> String:
    return String(s).pascal(delimiters, split_on_first_upper)


def snake(s: str,
          delimiters: List[str] = DEFAULT_DELIMITERS,
          split_on_first_upper: bool = False,
          title_case: bool = False) -> String:
    return String(s).snake(delimiters, split_on_first_upper, title_case)


class String(str):
    """
    Extends str
    """

    def __words__(self, delimiters: List[str] = DEFAULT_DELIMITERS, split_on_first_upper: bool = True) -> List[String]:
        """[summary]

        Args:
            delimiters (List[str], optional): Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): Defaults to True.

        Returns:
            :
        """

        if split_on_first_upper:
            s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", self)
            self = String(re.sub("([a-z0-9])([A-Z])", r"\1_\2", s))

        w = [String(w) for w in re.split(String.__regex_delimiters(delimiters), self) if w]
        return w
        return list(filter(None, w))

    @staticmethod
    def __escape_delimiters(delimiters: List[str] = DEFAULT_DELIMITERS) -> List[str]:
        return [delim if delim not in "[](){}*+?|^$.\\" else "\\" + delim for delim in delimiters]

    @staticmethod
    def __regex_delimiters(delimiters: List[str] = DEFAULT_DELIMITERS) -> str:
        return "|".join(String.__escape_delimiters(delimiters))

    @staticmethod
    def build(words: List[String],
              delimiter: str = "",
              word_modifier: Callable = None,
              first_word: str = "",
              last_word: str = "") -> String:
        """
        Constructs a string based on the specified words

        Args:
            words (List[str]): A list of str
            delimiter (str, optional): Defaults to "".
            word_modifier (Callable, optional): Defaults to None.
            first_word (str, optional): Defaults to "".
            last_word (str, optional): Defaults to "".

        Returns:
            String: [description]
        """
        return String(first_word + delimiter.join(word_modifier(w) if word_modifier else w for w in words) + last_word)

    def camel(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): Defaults to False.

        Returns:
            String: [description]
        """
        words = self.__words__(delimiters, split_on_first_upper)
        return String.build(
            words=words[1:],
            word_modifier=str.title,
            first_word=words[0].lower()
        ).replace(" ", "")

    def kebob(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = False,
              title_case: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): Defaults to False.
            title_case (bool, optional): Defaults to False.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            delimiter="-",
            word_modifier=str.title if title_case else str.lower
        ).replace(" ", "-").strip("-")

    def pascal(self,
               delimiters: List[str] = DEFAULT_DELIMITERS,
               split_on_first_upper: bool = True) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): Defaults to True.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            word_modifier=str.title
        ).replace(" ", "")

    def snake(self,
              delimiters: List[str] = DEFAULT_DELIMITERS,
              split_on_first_upper: bool = True,
              title_case: bool = False) -> String:
        """[summary]

        Args:
            delimiters (List[str], optional): Defaults to DEFAULT_DELIMITERS.
            split_on_first_upper (bool, optional): Defaults to True.
            title_case (bool, optional): Defaults to False.

        Returns:
            String: [description]
        """
        return String.build(
            words=self.__words__(delimiters, split_on_first_upper),
            delimiter="_",
            word_modifier=str.title if title_case else str.lower
        ).replace(" ", "_").strip("_")

# region Overrides

    # NOTE: Type type overrides below are necessary to pass mypy checks, because there was no apparent fix

    def capitalize(self) -> String:
        return String(super().capitalize())

    def casefold(self) -> String:
        return String(super().casefold())

    def center(self, __width: int, __fillchar: str = "") -> String:
        return String(super().center(__width, __fillchar))

    def expandtabs(self, tabsize: int = 8) -> String:
        return String(super().expandtabs(tabsize))

    def format(self, *args: object, **kwargs: object) -> String:
        return String(super().format(*args, **kwargs))

    def format_map(self, map: dict) -> String:  # type: ignore
        return String(super().format_map(map))

    def join(self, __iterable: Iterable[str]) -> String:
        return String(super().join(__iterable))

    def ljust(self, __width: int, __fillchar: str = "") -> String:
        return String(super().ljust(__width, __fillchar))

    def lower(self) -> String:
        return String(super().lower())

    def lstrip(self, __chars: Union[str, None] = None) -> String:
        return String(super().lstrip(__chars))

    def partition(self, __sep: str) -> Tuple[String, String, String]:
        part = super().partition(__sep)
        return (String(part[0]), String(part[1]), String(part[2]))

    if sys.version_info >= (3, 9):
        def removeprefix(self, __prefix: str) -> String:
            return String(super().removeprefix(__prefix))

        def removesuffix(self, __suffix: str) -> String:
            return String(super().removesuffix(__suffix))

    def replace(self, __old: str, __new: str, __count: int = -1) -> String:
        return String(super().replace(__old, __new, __count))

    def rjust(self, __width: int, __fillchar: str = "") -> String:
        return String(super().rjust(__width, __fillchar))

    def rpartition(self, __sep: str) -> Tuple[String, String, String]:
        r_part = super().rpartition(__sep)
        return (String(r_part[0]), String(r_part[1]), String(r_part[2]))

    def rsplit(self, sep: Union[str, None] = None, maxsplit: int = -1) -> List[String]:  # type: ignore
        return [String(s) for s in super().rsplit(sep, maxsplit)]

    def rstrip(self, __chars: Union[str, None] = None) -> String:
        return String(super().rstrip(__chars))

    def split(self, sep: Union[str, None] = None, maxsplit: int = -1) -> List[String]:  # type: ignore
        return [String(s) for s in super().split(sep, maxsplit)]

    def splitlines(self, keepends: bool = False) -> List[String]:  # type: ignore
        return [String(s) for s in super().splitlines(keepends)]

    def strip(self, __chars: Union[str, None] = None) -> String:
        return String(super().strip(__chars))

    def swapcase(self) -> String:
        return String(super().swapcase())

    def title(self) -> String:
        return String(super().title())

    def translate(self, __table: Union[Mapping[int, Union[int, str, None]], Sequence[Union[int, str, None]]]) -> String:
        return String(super().translate(__table))

    def upper(self) -> String:
        return String(super().upper())

    def zfill(self, __width: int) -> String:
        return String(super().zfill(__width))

    # region Magic Methods

    def __add__(self, s: str) -> String:
        return String(super().__add__(s))

    def __mul__(self, n: int) -> String:
        return String(super().__mul__(n))

    def __rmul__(self, n: int) -> String:
        return String(super().__rmul__(n))

    # endregion

# endregion

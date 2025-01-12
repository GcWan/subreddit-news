from typing import TypedDict, NotRequired, List


class Feed(TypedDict):
    url: str
    block: NotRequired[List[str]]


class Cycle(TypedDict):
    check_interval: int
    feeds: List[Feed]
    flair: NotRequired[str]


class SubredditConfig(TypedDict):
    cycles: List[Cycle]
    name: str

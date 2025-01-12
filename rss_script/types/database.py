from typing import TypedDict, List, Dict, Optional


class UpdateEntry(TypedDict):
    update_time: int
    update_index: int
    listening: bool


class RssSource(TypedDict):
    last_modified: Optional[str]
    etag: Optional[str]
    last_id: str


class SubredditData(TypedDict):
    update_list: List[UpdateEntry]
    rss_sources: Dict[str, RssSource]


Database = Dict[str, SubredditData]

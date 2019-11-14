"""
This module contains data classes to work with feeds.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    title: str = "no title"
    link: str = "no link"
    author: str = "no author"
    published: str = "no date"
    description: str = "description"
    img_links: List[str] = field(default_factory=list)


@dataclass
class Feed:
    title: str = "no title"
    link: str = "no link"
    items: List[Item] = field(default_factory=list)

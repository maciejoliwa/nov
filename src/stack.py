from dataclasses import dataclass, field
from typing import List, NoReturn, Optional


@dataclass
class NovStack:

    _top: Optional[int] = 0
    _items: List[int] = field(default_factory=lambda: list([]))

    def push(self, to_push: int) -> NoReturn:
        self._items[self._top] = to_push
        self._top = self._top + 1

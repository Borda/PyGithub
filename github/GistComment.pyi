from datetime import datetime
from typing import Any, Dict

from github.NamedUser import NamedUser

from github.GithubObject import CompletableGithubObject

class GistComment(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def body(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def id(self) -> int: ...
    def delete(self) -> None: ...
    def edit(self, body: str) -> None: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> NamedUser: ...

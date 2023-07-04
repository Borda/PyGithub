from typing import Any, Dict, List

from github.CommitStatus import CommitStatus
from github.Repository import Repository

from github.GithubObject import NonCompletableGithubObject

class CommitCombinedStatus(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def commit_url(self) -> str: ...
    @property
    def repository(self) -> Repository: ...
    @property
    def sha(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def statuses(self) -> List[CommitStatus]: ...
    @property
    def total_count(self) -> int: ...
    @property
    def url(self) -> str: ...

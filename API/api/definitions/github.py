import strawberry
from typing import List, Union
import datetime


@strawberry.type
class GithubOverview:
    languages: List[str]
    commits: int
    forks: int
    stars: int
    watches: int
    contributors: int
    pull_requests: int
    issues: int


@strawberry.type
class GithubAnalyticsPerTime:
    commits: int
    forks: int
    stars: int
    pull_requests: int
    issues: int
    watches: int
    lp_day_of_week: Union[str, None]
    lp_day: Union[int, None]
    last_push_date: Union[datetime.datetime, None]


@strawberry.type
class GithubAnalyticsPerRepo:
    commits: int
    forks: int
    stars: int
    contributors: int
    pull_requests: int
    issues: int
    repo_name: str


@strawberry.type
class PerRepo:
    repo: List[GithubAnalyticsPerRepo]


@strawberry.type
class PerTime:
    repo: List[GithubAnalyticsPerTime]

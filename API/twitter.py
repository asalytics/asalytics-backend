from typing import Any, Dict, List, Mapping, Union
from pyparsing import Optional
import strawberry
from datetime import datetime
from strawberry.scalars import JSON


@strawberry.type
class TwitterOverview:
    asaID: str
    tweetTotal: int 
    likeTotal: int
    retweetTotal: int 
    sentimentTotal: float 

@strawberry.type
class TwitterWeekdayAnalytics:
    asaID_w: Union[str, None]
    likesCount_w: Union[List[JSON], None]
    retweetsCount_w: Union[List[JSON], None]
    sentimentScore_w: Union[List[JSON], None]

@strawberry.type
class TwitterHourAnalytics:
    asaID_h: Union[str, None]
    likesCount_h: Union[List[JSON], None]
    retweetsCount_h: Union[List[JSON], None]
    sentimentScore_h: Union[List[JSON], None]



@strawberry.type
class TwitterAnalytics:
    asaID: Union[str, None]
    likesCount: Union[List[JSON], None]
    retweetsCount: Union[List[JSON], None]
    sentimentScore: Union[List[JSON], None]
    # weekday: List[str]
    # hour: List[int]

@strawberry.type
class response(TwitterAnalytics,TwitterWeekdayAnalytics,TwitterHourAnalytics):
    pass

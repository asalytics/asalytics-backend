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
    # asaID: Union[str, None]
    posted_at: Union[datetime, None]
    dow: Union[int, None]
    hour: Union[int, None]
    likes: int
    retweets: int
    sentiment: float

@strawberry.type
class response:
    asaID: Union[str, None]
    results: List[TwitterAnalytics]

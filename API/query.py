from typing import List, Union
from urllib import response
from fastapi import status, HTTPException
import strawberry
from models import Twitter
from twitter import TwitterAnalytics, TwitterOverview, Response
from tortoise.functions import Avg, Count, Sum
from dacite import from_dict

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# def customSum(element:list, mt:int)

@strawberry.type
class Query:
    @strawberry.field 
    async def twitterOverview(self, asaID:str) -> TwitterOverview:

        """
        Resolver to generate summary overview for all twitter posts of a given ASA.
        params
            asaID
        returns
            List[TwitterOverview]
        """
        result = await Twitter.filter(asa_id=asaID).values() 
        
        result = {key: [i[key] for i in result] for key in result[0]}
        result = AttrDict(result)

        return TwitterOverview(
            asaID = result['asa_id'][0],
            tweetTotal = len(result['tweet']),
            likeTotal = sum(result['likes']),
            retweetTotal = sum(result['retweets']),
            sentimentTotal = sum(result['sentiment_score'])
        )

    @strawberry.field
    async def twitterAnalytics(self, asaID:str, 
                                startDate:str = '2021-03-01', #to be modified to datetime.now
                                endDate:str = '2021-03-21',  #to be modified to timedelta
                                weekday: bool=False, 
                                hour: bool=False) -> Response:

        """
        Resolver to generate Twitter analytics for an ASA depending on parameters. 
        params
            asaID
            startDate   default = datetime.datetime.now
            endDate     default = datetime.datetime.now - datetime.timedelta(7)
            weeekday    default = False
            hour        default = False
        returns
            List[Response]

        """
        
        if weekday and hour:

            raise Exception("Error! Analyze weekday or hour")

        if weekday:
            
            result = await Twitter.\
                filter(asa_id = asaID).\
                filter(posted_at__range = [startDate, endDate]).\
                annotate(likes = Sum("likes"), retweets = Sum('retweets'),
                sentiment = Sum("sentiment_score")).\
                group_by("dow").\
                values("dow", "likes", "retweets", "sentiment")

            

        if hour:
            result = await Twitter.\
                filter(asa_id = asaID).\
                filter(posted_at__range = [startDate, endDate]).\
                annotate(likes = Sum("likes"), retweets = Sum('retweets'),
                sentiment = Sum("sentiment_score")).\
                group_by("hour").\
                values("hour", "likes", "retweets", "sentiment")
            


        if ((hour == False) & (weekday == False)):
            result = await Twitter.filter(asa_id = asaID).filter(posted_at__range = [startDate, endDate]).\
                annotate(likes=Sum("likes"), retweets=Sum("retweets"), sentiment= Sum("sentiment_score")).\
                group_by("posted_at").\
                values("posted_at", "likes", "retweets", "sentiment")


        result = [from_dict(data_class=TwitterAnalytics, data=x) for x in result]
        
        return response(
                asaID = asaID,
                results = result
            
            
            

        )

schema = strawberry.Schema(query = Query)




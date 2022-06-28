from typing import List, Union
from urllib import response
from fastapi import status, HTTPException
import strawberry
from models import Twitter
from twitter import TwitterOverview, TwitterAnalytics, response
from tortoise.functions import Avg, Count, Sum

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# def customSum(element:list, mt:int)

@strawberry.type
class Query:
    @strawberry.field 
    async def twitterOverview(self, asaID:str) -> TwitterOverview:
        result = await Twitter.filter(asa_id=asaID).values()
        # print(result)
        # print(result['asa_id'])
        # print(len(result['tweet']))
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
    async def twitterAnalytics(self, asaID:str, startDate:str = '2021-03-01', endDate:str = '2021-03-21', weekday: bool=False, hour: bool=False) -> response:
        
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
            print(result)

            return response(
                asaID_h=None,
                likesCount_h=None,
                retweetsCount_h=None,
                sentimentScore_h=None,
                asaID_w = asaID,
                likesCount_w= result,
                retweetsCount_w = result,
                sentimentScore_w = result,
                asaID = None,
                likesCount = None,
                retweetsCount = None,
                sentimentScore = None
                
            
            )

        if hour:
            result = await Twitter.\
                filter(asa_id = asaID).\
                filter(posted_at__range = [startDate, endDate]).\
                annotate(likes = Sum("likes"), retweets = Sum('retweets'),
                sentiment = Sum("sentiment_score")).\
                group_by("hour").\
                values("hour", "likes", "retweets", "sentiment")
            return response(
                asaID_h=result,
                likesCount_h=result,
                retweetsCount_h=result,
                sentimentScore_h=result,
                asaID_w = None,
                likesCount_w= None,
                retweetsCount_w = None,
                sentimentScore_w = None,
                asaID = None,
                likesCount = None,
                retweetsCount = None,
                sentimentScore = None
            )


        result = await Twitter.filter(asa_id = asaID).filter(posted_at__range = [startDate, endDate]).values()
        result = {key: [i[key] for i in result] for key in result[0]}
        print(result)
        return response(
            asaID = asaID,
            likesCount = result['likes'],
            retweetsCount = result['retweets'],
            sentimentScore = result['sentiment_score'],
            asaID_w = None,
            likesCount_w= None,
            retweetsCount_w = None,
            sentimentScore_w = None,
            asaID_h=None,
            likesCount_h=None,
            retweetsCount_h=None,
            sentimentScore_h=None,
            
            
            # hour = result['hour'],
            # weekday = result['dow']
            

        )

schema = strawberry.Schema(query = Query)




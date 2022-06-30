from typing import List, Union
from urllib import response
from fastapi import status, HTTPException
import strawberry
from models import Twitter
from twitter import  TwitterAnalytics, TwitterOverview
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
    async def twitterAnalytics(self, asaID:str, startDate:str = '2021-03-01', endDate:str = '2021-03-21', weekday: bool=False, hour: bool=False) -> TwitterAnalytics:
        
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

            return TwitterAnalytics(
                
                asaID = asaID,
                results = result
            
            )

        if hour:
            result = await Twitter.\
                filter(asa_id = asaID).\
                filter(posted_at__range = [startDate, endDate]).\
                annotate(likes = Sum("likes"), retweets = Sum('retweets'),
                sentiment = Sum("sentiment_score")).\
                group_by("hour").\
                values("hour", "likes", "retweets", "sentiment")
            return TwitterAnalytics(

               asaID = asaID,
                results = result
                
            )


        result = await Twitter.filter(asa_id = asaID).filter(posted_at__range = [startDate, endDate]).\
            annotate(likes=Sum("likes"), retweets=Sum("retweets"), sentiment= Sum("sentiment_score")).\
            group_by("posted_at").\
            values("posted_at", "likes", "retweets", "sentiment")

        result_at = [str(i["posted_at"]) for i in result]
        
        counter = 0
        for r in result:
            r["posted_at"] = result_at[counter]
            counter+=1 

        # [print(i["posted_at"]) for i in result]
        # result = {key: [i[key] for i in result] for key in result[0]}
        # print(result)
        return TwitterAnalytics(
                asaID = asaID,
                results = result
                
            
            
            # hour = result['hour'],
            # weekday = result['dow']
            

        )

schema = strawberry.Schema(query = Query)




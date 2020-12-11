import requests
import os
import api_credentials

tweet_fields = "tweet.fields=attachments,author_id,context_annotations,created_at,entities,geo,id,in_reply_to_user_id,lang," \
               "possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld"

# source code forked from the twitter's official documentation
# with some additional changes
# Link to the source code : https://github.com/twitterdev/Twitter-API-v2-sample-code

class TweetLookupHelper:
    @staticmethod
    def auth():
        return api_credentials.BEARER_TOKEN

    @staticmethod
    def create_url():
        ids = "ids=1278747501642657792,1255542774432063488"
        url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
        return url

    @staticmethod
    def create_headers(bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers

    @staticmethod
    def connect_to_endpoint(url, headers):
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()


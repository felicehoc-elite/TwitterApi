import requests
import os
import json

class TwitterApiHelper:
    def auth(self):
        return os.environ.get("BEARER_TOKEN")

    def create_url(self):
        tweet_fields = "tweet.fields=lang,author_id"
        # Tweet fields are adjustable.
        # Options include:
        # attachments, author_id, context_annotations,
        # conversation_id, created_at, entities, geo, id,
        # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
        # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
        # source, text, and withheld
        ids = "ids=1278747501642657792,1255542774432063488"
        # You can adjust ids to include a single Tweets.
        # Or you can add to up to 100 comma-separated IDs
        url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
        return url

    def create_headers(self,bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers

    def connect_to_endpoint(self,url, headers):
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()


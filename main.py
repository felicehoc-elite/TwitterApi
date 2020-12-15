from TweetsApiHelper import TweetLookupHelper as tweets_helper
import json


def main():
    bearer_token = tweets_helper.auth()
    url = tweets_helper.create_url()
    headers = tweets_helper.create_headers(bearer_token)
    json_response = tweets_helper.connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
from TweetsApiHelper import TweetLookupHelper as tweets_helper
import json
from JsonDataParser import TweetsDataParser
from CrudRepositories import *

def main():
    bearer_token = tweets_helper.auth()
    url = tweets_helper.create_url()
    headers = tweets_helper.create_headers(bearer_token)
    json_response = tweets_helper.connect_to_endpoint(url, headers)

    tweet_repository = TweetRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    annotation_repo = AnnotationRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    hashtag_repo = HashtagRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    url_repo = UrlRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    image_repo = ImageRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    entity_repo = EntityRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    domain_repo = DomainRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    context_entity_repo = ContextEntityRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")
    context_annotation_repo = ContextAnnotationRepository(host = "localhost", user = "root", password = "", database = "TweeterApiData")

    tweet = TweetsDataParser.parse_Tweet(json_response["data"][0])
    """ insert tweet """
    tweet_id = tweet_repository.insert(tweet)
    """inserting annotations"""
    annotations = TweetsDataParser.parse_annotations(json_response["data"][0])
    for entity,annotation in annotations:
        """insert annotation"""
        annotation_id = annotation_repo.insert(annotation)
        """set the annotation id in entity"""
        entity.annotation_id = annotation_id
        entity.tweet_id = tweet_id
        """insert entity"""
        entity_repo.insert(entity)

    hashtags = TweetsDataParser.parse_hashtags(json_response["data"][0])
    for entity,hashtag in hashtags:
        """insert hashtag"""
        hashtag_id = hashtag_repo.insert(hashtag)
        """set the hashtag id in entity"""
        entity.hashtag_id = hashtag_id
        entity.tweet_id = tweet_id
        """insert entity"""
        entity_repo.insert(entity)


    urls = TweetsDataParser.parse_urls(json_response["data"][0])
    for entity,url,images in urls:
        """insert url"""
        url_id = url_repo.insert(url)
        """set the url id in entity"""
        entity.url_id = url_id
        entity.tweet_id = tweet_id
        """insert entity"""
        entity_repo.insert(entity)
        """set the urlid in images"""
        """insert images"""
        for image in images:
            image.url_id = url_id
            image_repo.insert(image)



if __name__ == "__main__":
    main()
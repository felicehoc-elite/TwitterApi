"""
tweet_id, created_at, lang, possibly_sensitive, source,
                 text, like_count, quote_count, reply_count, retweet_count
"""
class Tweet:
    def __init__(self, *args, **kwargs) -> None:
        self.tweet_id = kwargs.get("tweet_id")
        self.created_at = kwargs.get("created_at")
        self.lang = kwargs.get("lang")
        self.possibly_sensitive = kwargs.get("possibly_sensitive")
        self.source = kwargs.get("source")
        self.text = kwargs.get("text")
        self.like_count = kwargs.get("like_count")
        self.quote_count = kwargs.get("quote_count")
        self.reply_count = kwargs.get("reply_count")
        self.retweet_count = kwargs.get("retweet_count")


class Annotation:
    """
    annotation_id, normalized_text, probability
    """
    def __init__(self,*args, **kwargs) -> None:
        self.annotation_id = kwargs.get("annotation_id")
        self.normalized_text = kwargs.get("normalized_text")
        self.probability = kwargs.get("probability")


class Hashtag:
    """
    hashtag_id, tag
    """
    def __init__(self, *args,**kwargs) -> None:
        self.hashtag_id = kwargs.get("hashtag_id")
        self.tag = kwargs.get("tag")


class Url:
    """
    url_id, description, expanded_url, status, title, unwound_url
    """
    def __init__(self, *args, **kwargs) -> None:
        self.url_id = kwargs.get("url_id")
        self.description = kwargs.get("description")
        self.expanded_url = kwargs.get("expanded_url")
        self.status = kwargs.get("status")
        self.title = kwargs.get("title")
        self.unwound_url = kwargs.get("unwound_url")


class Image:
    """
    image_id, url, height,width,url_id
    """
    def __init__(self,*args,**kwargs) -> None:
        self.image_id = kwargs.get("image_id")
        self.url = kwargs.get("url")
        self.height = kwargs.get("height")
        self.width = kwargs.get("width")
        self.url_id = kwargs.get("url_id")


class Entity:
    """
    tweet_id, annotation_id, hashtag_id, url_id, end, start
    """
    def __init__(self,*args,**kwargs) -> None:
        self.tweet_id = kwargs.get("tweet_id")
        self.annotation_id = kwargs.get("annotation_id")
        self.hashtag_id = kwargs.get("hashtag_id")
        self.url_id = kwargs.get("url_id")
        self.end = kwargs.get("end")
        self.start = kwargs.get("start")


class Domain:
    """
    domain_id, name, description
    """
    def __init__(self, *args, **kwargs) -> None:
        self.domain_id = kwargs.get("domain_id")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")


class ContextEntity:
    """
    context_entity_id, name, description
    """
    def __init__(self, *args, **kwargs) -> None:
        self.context_entity_id = kwargs.get("context_entity_id")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")


class ContextAnnotation:
    """
    tweet_id, domain_id, context_entity_id
    """
    def __init__(self, *args, **kwargs) -> None:
        self.tweet_id = kwargs.get("tweet_id")
        self.domain_id = kwargs.get("domain_id")
        self.context_entity_id = kwargs.get("context_entity_id")

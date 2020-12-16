
class Tweet:
    def __init__(self, tweet_id, created_at, lang, possibly_sensitive, source,
                 text, like_count, quote_count, reply_count, retweet_count) -> None:
        self.tweet_id = tweet_id
        self.created_at = created_at
        self.lang = lang
        self.possibly_sensitive = possibly_sensitive
        self.source = source
        self.text = text
        self.like_count = like_count
        self.quote_count = quote_count
        self.reply_count = reply_count
        self.retweet_count = retweet_count


class Annotation:

    def __init__(self,annotation_id, normalized_text, probability) -> None:
        self.annotation_id = annotation_id
        self.normalized_text = normalized_text
        self.probability = probability


class Hashtag:
    def __init__(self, hashtag_id, tag) -> None:
        self.hashtag_id = hashtag_id
        self.tag = tag


class Url:
    def __init__(self, url_id, description, expanded_url, status, title, unwound_url) -> None:
        self.url_id = url_id
        self.description = description
        self.expanded_url = expanded_url
        self.status = status
        self.title = title
        self.unwound_url = unwound_url


class Image:
    def __init__(self,image_id, url, height,width,url_id) -> None:
        self.image_id = image_id
        self.url = url
        self.height = height
        self.width = width
        self.url_id = url_id


class Entity:
    def __init__(self,tweet_id, annotation_id, hashtag_id, url_id, end, start) -> None:
        self.tweet_id = tweet_id
        self.annotation_id = annotation_id
        self.hashtag_id = hashtag_id
        self.url_id = url_id
        self.end = end
        self.start = start


class Domain:
    def __init__(self, domain_id, name, description) -> None:
        self.domain_id = domain_id
        self.name = name
        self.description = description


class ContextEntity:
    def __init__(self, context_entity_id, name, description) -> None:
        self.context_entity_id = context_entity_id
        self.name = name
        self.description = description


class ContextAnnotation:
    def __init__(self, tweet_id, domain_id, context_entity_id) -> None:
        self.tweet_id = tweet_id
        self.domain_id = domain_id
        self.context_entity_id = context_entity_id

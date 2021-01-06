import DBManager
from Model import *


class TweetRepository(DBManager.MySqlDBManager):
    def insert(self, tweet: Tweet):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Tweet (tweet_id, created_at, lang, possibly_sensitive, source, " \
              "text, like_count, quote_count, reply_count, retweet_count) " \
              "VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        val = (tweet.tweet_id,tweet.created_at, tweet.lang, tweet.possibly_sensitive, tweet.source,
               tweet.text, tweet.like_count, tweet.quote_count, tweet.reply_count, tweet.retweet_count)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        self.close()
        return id

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Tweet")
        return list(cursor.fetchall())


class AnnotationRepository(DBManager.MySqlDBManager):
    def insert(self, annotation: Annotation):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Annotation (annotation_id, normalized_text, probability)" \
              "VALUES (%s, %s, %s)"
        val = (annotation.annotation_id, annotation.normalized_text, annotation.probability)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        self.close()
        return id

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Annotation")
        return list(cursor.fetchall())


class HashtagRepository(DBManager.MySqlDBManager):
    def insert(self, hashtag: Hashtag):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Hashtag (hashtag_id, tag)" \
              "VALUES (%s, %s)"
        val = (hashtag.hashtag_id,hashtag.tag)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        self.close()
        return id

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Hashtag")
        return list(cursor.fetchall())


class UrlRepository(DBManager.MySqlDBManager):
    def insert(self, url: Url):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Url (url_id, description, expanded_url, status, title, unwound_url)" \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        val = (url.url_id, url.description, url.expanded_url,url.status, url.title, url.unwound_url)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        self.close()
        return id

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Url")
        return list(cursor.fetchall())


class ImageRepository(DBManager.MySqlDBManager):
    def insert(self, image: Image):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Image (image_id, url, height,width,url_id)" \
              "VALUES (%s, %s, %s, %s, %s)"
        val = (image.image_id, image.url, image.height, image.width, image.url_id)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        self.close()
        return id

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Image")
        return list(cursor.fetchall())

class EntityRepository(DBManager.MySqlDBManager):
    def insert(self, entity: Entity):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Entity (tweet_id, annotation_id, hashtag_id, url_id, end, start)" \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        val = (entity.tweet_id, entity.annotation_id, entity.hashtag_id, entity.url_id, entity.end, entity.start)
        cursor.execute(sql, val)
        self.close()

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Entity")
        return list(cursor.fetchall())


class DomainRepository(DBManager.MySqlDBManager):
    def insert(self, domain: Domain):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO Domain (domain_id, name, description)" \
              "VALUES (%s, %s, %s)"
        val = (domain.domain_id, domain.name, domain.description)
        cursor.execute(sql, val)
        self.close()

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Domain")
        return list(cursor.fetchall())


class ContextEntityRepository(DBManager.MySqlDBManager):
    def insert(self, context_entity: ContextEntity):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO ContextEntity (context_entity_id, name, description)" \
              "VALUES (%s, %s, %s)"
        val = (context_entity.context_entity_id, context_entity.name, context_entity.description)
        cursor.execute(sql, val)
        self.close()

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ContextEntity")
        return list(cursor.fetchall())


class ContextAnnotationRepository(DBManager.MySqlDBManager):
    def insert(self, context_annotation: ContextAnnotation):
        self.connect()
        cursor = self.connection.cursor()
        sql = "INSERT INTO ContextAnnotation (tweet_id, domain_id, context_entity_id)" \
              "VALUES (%s, %s, %s)"
        val = ( context_annotation.tweet_id,  context_annotation.domain_id, context_annotation.context_entity_id)
        cursor.execute(sql, val)
        self.close()

    def fetch_all(self)->list:
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ContextAnnotation")
        return list(cursor.fetchall())
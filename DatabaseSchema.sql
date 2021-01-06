CREATE TABLE IF NOT EXISTS Tweet (
    tweet_id INT(15) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    lang VARCHAR(30) NOT NULL,
    possibly_sensitive BOOLEAN,
    source VARCHAR(200),
    text VARCHAR(500),
    like_count int(6) DEFAULT 0,
    quote_count int(6) DEFAULT 0,
    reply_count int(6) DEFAULT 0,
    retweet_count int(6) DEFAULT 0
);
CREATE TABLE IF NOT EXISTS Annotation (
    annotation_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    normalized_text VARCHAR(50),
    probability FLOAT DEFAULT 0
);
CREATE TABLE IF NOT EXISTS Hashtag (
    hashtag_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tag VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS Url (
    url_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(200),
    expanded_url VARCHAR(200),
    status int(3) DEFAULT 0,
    title VARCHAR(200),
    unwound_url VARCHAR(200)
);
CREATE TABLE IF NOT EXISTS Image(
    image_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    url      VARCHAR(200),
    height   int(6) DEFAULT 0,
    width    int(6) DEFAULT 0,
    url_id   INT(6),
    CONSTRAINT urlFK FOREIGN KEY (url_id) REFERENCES Url(url_id)
);
CREATE TABLE IF NOT EXISTS Entity (
    tweet_id INT(6),
    annotation_id INT(6),
    hashtag_id INT(6),
    url_id INT(6),
    end INT(3) DEFAULT 0,
    start INT(3) DEFAULT 0,
    CONSTRAINT tweetFK FOREIGN KEY (tweet_id) REFERENCES Tweet(tweet_id),
    CONSTRAINT annotationFK FOREIGN KEY (annotation_id) REFERENCES Annotation(annotation_id),
    CONSTRAINT hashtagFK FOREIGN KEY (hashtag_id) REFERENCES Hashtag(hashtag_id),
    CONSTRAINT urlFK FOREIGN KEY (url_id) REFERENCES Url(url_id)
);
CREATE TABLE IF NOT EXISTS domain (
    domain_id INT(15) PRIMARY KEY,
    name VARCHAR(200),
    description VARCHAR(1000)
);
CREATE TABLE IF NOT EXISTS ContextEntity (
    context_entity_id INT(15) PRIMARY KEY,
    name VARCHAR(200),
    description VARCHAR(1000)
);
CREATE TABLE IF NOT EXISTS ContextAnnotation(
    tweet_id INT(6),
    domain_id INT(6),
    context_entity_id INT(6),
    CONSTRAINT tweetFK FOREIGN KEY (tweet_id) REFERENCES Tweet(tweet_id),
    CONSTRAINT domainFK FOREIGN KEY (domain_id) REFERENCES domain(domain_id),
    CONSTRAINT contextEntityFK FOREIGN KEY (context_entity_id) REFERENCES ContextEntity(context_entity_id)
);
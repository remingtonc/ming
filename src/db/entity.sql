CREATE TABLE activity (
    id  BIGINT AUTO_INCREMENT NOT NULL,
    happiness   TINYINT NOT NULL,
    productivity    TINYINT NOT NULL,
    start_time  TIMESTAMP NOT NULL,
    end_time    TIMESTAMP,
    name    VARCHAR(140),
    description VARCHAR(1500),
    PRIMARY KEY(id),
    INDEX(happiness),
    INDEX(productivity),
    INDEX(start_time),
    INDEX(end_time),
    INDEX(name)
);

CREATE TABLE link (
    url VARCHAR(500),
    name    VARCHAR(140),
    PRIMARY KEY(url),
    INDEX(name)
);

CREATE TABLE tag (
    id  VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE priority (
    tag_id  VARCHAR(50) NOT NULL,
    rank    INTEGER NOT NULL,
    time_ratio  REAL NOT NULL,
    PRIMARY KEY(tag_id),
    FOREIGN KEY(tag_id)
        REFERENCES tag(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

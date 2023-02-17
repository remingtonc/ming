-- Deploy ming:initial to pg

BEGIN;

CREATE SCHEMA ming;

CREATE TABLE ming.user (
    user_id bigserial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE ming.record (
    record_id bigserial NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT fk_user_owns_record
        FOREIGN KEY(user_id)
        REFERENCES ming.user(user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(record_id)
);

CREATE TABLE ming.record_story (
    record_story_id bigint NOT NULL,
    content text NOT NULL,
    CONSTRAINT fk_record_story_record_id
        FOREIGN KEY(record_story_id)
        REFERENCES ming.record(record_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(record_story_id)
);

CREATE TABLE ming.record_image (
    record_image_id bigint NOT NULL,
    path text NOT NULL,
    CONSTRAINT fk_record_image_record_id
        FOREIGN KEY(record_image_id)
        REFERENCES ming.record(record_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(record_image_id)
);

CREATE TABLE ming.record_activity (
    record_activity_id bigint NOT NULL,
    name text NOT NULL,
    description text,
    happiness smallint,
    productivity smallint,
    start_time timestamptz NOT NULL DEFAULT NOW()::timestamptz,
    end_time timestamptz,
    CONSTRAINT fk_record_activity_record_id
        FOREIGN KEY(record_activity_id)
        REFERENCES ming.record(record_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(record_activity_id)
);

CREATE TABLE ming.record_link (
    record_link_id bigint NOT NULL,
    name text,
    url text NOT NULL,
    CONSTRAINT fk_record_link_record_id
        FOREIGN KEY(record_link_id)
        REFERENCES ming.record(record_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(record_link_id)
);

CREATE TABLE ming.tag (
    tag_id bigserial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY(tag_id),
    UNIQUE(name)
);

CREATE TABLE ming.record_has_tag (
    tag_id bigint NOT NULL,
    record_id bigint NOT NULL,
    CONSTRAINT fk_record_has_tag_tag_id
        FOREIGN KEY(tag_id)
        REFERENCES ming.tag(tag_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_record_has_tag_record_id
        FOREIGN KEY(record_id)
        REFERENCES ming.record(record_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    PRIMARY KEY(tag_id, record_id)
);

COMMIT;

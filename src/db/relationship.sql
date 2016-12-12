CREATE TABLE activity_has_link (
    activity_id BIGINT NOT NULL,
    link_id BIGINT NOT NULL,
    PRIMARY KEY(activity_id, link_id),
    FOREIGN KEY activity_id
        REFERENCES activity(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY link_id
        REFERENCES link(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE activity_has_tag (
    activity_id BIGINT NOT NULL,
    tag_id  VARCHAR(50) NOT NULL,
    PRIMARY KEY(activity_id, tag_id),
    FOREIGN KEY(activity_id)
        REFERENCES activity(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(tag_id)
        REFERENCES tag(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE tag_implies_tag (
    tag_id  VARCHAR(50) NOT NULL,
    implied_id  VARCHAR(50) NOT NULL,
    PRIMARY KEY(tag_id, implied_id),
    FOREIGN KEY(tag_id)
        REFERENCES tag(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(implied_id)
        REFERENCES tag(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

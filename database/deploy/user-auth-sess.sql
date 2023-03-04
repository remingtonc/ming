-- Deploy ming:user-auth-sess to pg

BEGIN;

CREATE TABLE ming.user_session (
    user_id bigint NOT NULL,
    session_id uuid NOT NULL DEFAULT gen_random_uuid(),
    create_time timestamptz NOT NULL DEFAULT NOW()::timestamptz,
    CONSTRAINT fk_user_user_sessions
        FOREIGN KEY(user_id)
        REFERENCES ming.user(user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,    
    PRIMARY KEY(user_id, session_id)
);

COMMIT;

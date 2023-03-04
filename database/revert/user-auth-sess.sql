-- Revert ming:user-auth-sess from pg

BEGIN;

DROP TABLE ming.user_session;

COMMIT;

-- Revert ming:initial from pg

BEGIN;

DROP SCHEMA ming CASCADE;

COMMIT;

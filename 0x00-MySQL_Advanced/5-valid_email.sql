-- this script resets the attribute valid_email only,
-- when the email has been changed

CREATE OR REPLACE FUNCTION reset_valid_email()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.email != OLD.email THEN
        NEW.valid_email = 0;
    END IF;
    RETURN NEW;
END;

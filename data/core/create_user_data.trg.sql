
CREATE OR REPLACE FUNCTION create_user_data()
RETURNS trigger AS $$
BEGIN
    INSERT INTO user_data(user_id, phone, birth_date, avatar, bio)
    VALUES (
        NEW.id,
        NULL,
        NULL,
        'default_user.png',
        'Hi!'
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Next, create the trigger that calls the function after a new row is inserted into auth_user
CREATE TRIGGER create_user_data_AI
AFTER INSERT ON auth_user
FOR EACH ROW
EXECUTE FUNCTION create_user_data();

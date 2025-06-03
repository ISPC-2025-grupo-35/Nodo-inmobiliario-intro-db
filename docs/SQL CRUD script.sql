USE nodo_inmobiliario;

INSERT INTO users (user_id, name, surname, email, password, role, register_date)
VALUES ('123e4567', 'Santiago', 'Perez', 'santiago1@email.com', 'santiagopassword123', 'TENANT', '02-06-2025');

SELECT user_id, name, surname, email, role, register_date
FROM users
WHERE enabled = TRUE;

SELECT user_id, name, surname, email, register_date
FROM users
WHERE role = 'LANDLORD'
ORDER BY register_date DESC;

UPDATE users
SET email = 'santiago2@email.com'
WHERE user_id = '123e4567';

UPDATE users
SET enabled = FALSE
WHERE user_id = '123e4567';


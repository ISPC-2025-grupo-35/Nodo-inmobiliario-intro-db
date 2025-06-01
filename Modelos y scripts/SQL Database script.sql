CREATE DATABASE nodo_inmobiliario;

CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    register_date DATE NOT NULL,
    enabled BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS user_roles (
    role_name VARCHAR(50) NOT NULL PRIMARY KEY
);

INSERT INTO user_roles (role_name) VALUES
    ('ADMIN'),
    ('TENANT'),
    ('LANDLORD');

ALTER TABLE users
ADD CONSTRAINT fk_user_role
FOREIGN KEY (role)
REFERENCES user_roles(role_name);
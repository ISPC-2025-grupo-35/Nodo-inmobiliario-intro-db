#Creación y uso de basa de datos
CREATE DATABASE nodo_inmobiliario;
USE nodo_inmobiliario;

#Creación y población de Enums
CREATE TABLE Role_enum (
	name VARCHAR(50) PRIMARY KEY
);
INSERT INTO Role_enum (name)
VALUES ('admin'), ('tenant'), ('landlord');

CREATE TABLE Property_type_enum (
	name VARCHAR(50) PRIMARY KEY
);
INSERT INTO Property_type_enum (name)
VALUES  ('house'), ('appartment'), ('studio'), ('duplex'), ('cabain');

CREATE TABLE Operation_enum (
	name VARCHAR(50) PRIMARY KEY
);
INSERT INTO Operation_enum (name)
VALUES ('rent'), ('purchase'), ('both');

CREATE TABLE Status_enum (
	name VARCHAR(50) PRIMARY KEY
);
INSERT INTO Status_enum (name)
VALUES  ('available'), ('paused'), ('OTM');
    
#Creación de tabla user
CREATE TABLE User (
    user_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    register_date DATE NOT NULL,
    enabled BOOLEAN NOT NULL,
    FOREIGN KEY (role) REFERENCES Role_enum(name)
);

#Creación de tabla publication
CREATE TABLE Publication (
    publication_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    title VARCHAR(255) NOT NULL,
    publication_description TEXT NOT NULL,
    property_type VARCHAR(50) NOT NULL,
    operation VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    city VARCHAR(100) NOT NULL,
    sqr_mts FLOAT NOT NULL,
    spaces FLOAT NOT NULL,
    bedrooms INT NOT NULL,
    bathroom FLOAT NOT NULL,
    picture_url VARCHAR(255) NOT NULL,
    register_state DATE NOT NULL,
    property_status VARCHAR(50) NOT NULL,
    enabled BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (operation) REFERENCES Operation_enum(name),
    FOREIGN KEY (property_type) REFERENCES Property_type_enum(name),
    FOREIGN KEY (property_status) REFERENCES Status_enum(name)
);

#Creación de tabla address
CREATE TABLE Address (
    address_id VARCHAR(36) PRIMARY KEY,
    publication_id VARCHAR(36) UNIQUE NOT NULL,
    street VARCHAR(100) NOT NULL,
    number INT NOT NULL,
    letter CHAR(1),
    floor INT,
    neighborhood VARCHAR(100),
    FOREIGN KEY (publication_id) REFERENCES Publication(publication_id)
);

#Creación de tabla conversation
CREATE TABLE Conversation (
    conversation_id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(36) NOT NULL,
    landlord_id VARCHAR(36) NOT NULL,
    publication_id VARCHAR(36) NOT NULL,
    start_date DATE NOT NULL,
    enabled BOOLEAN NOT NULL,
    FOREIGN KEY (tenant_id) REFERENCES User(user_id),
    FOREIGN KEY (landlord_id) REFERENCES User(user_id),
    FOREIGN KEY (publication_id) REFERENCES Publication(publication_id)
);

#Creación de tabla message
CREATE TABLE Message (
    message_id VARCHAR(36) PRIMARY KEY,
    sender_id VARCHAR(36) NOT NULL,
    receiver_id VARCHAR(36) NOT NULL,
    conversation_id VARCHAR(36) NOT NULL,
    content TEXT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES User(user_id),
    FOREIGN KEY (receiver_id) REFERENCES User(user_id),
    FOREIGN KEY (conversation_id) REFERENCES Conversation(conversation_id)
);

#Población con datos
INSERT INTO User (user_id, name, surname, email, password, role, register_date, enabled)
VALUES 
('u1', 'Juan', 'Pérez', 'juan@example.com', 'hash123', 'tenant', '2025-06-01', TRUE),
('u2', 'Laura', 'García', 'laura@example.com', 'hash456', 'landlord', '2025-06-01', TRUE),
('u3', 'Pedro', 'Ruiz', 'pedro@example.com', 'hash789', 'tenant', '2025-06-02', TRUE),
('u4', 'Admin', 'Admin', 'admin@example.com', 'admin456', 'admin', '2025-06-03', TRUE);

INSERT INTO Publication (publication_id, user_id, title, publication_description, property_type, operation, price, city, sqr_mts, spaces, bedrooms, bathroom, picture_url, register_state, property_status, enabled)
VALUES 
('p1', 'u2', 'Depto 2 ambientes', 'Luminoso y bien ubicado', 'appartment', 'rent', 150000, 'Buenos Aires', 50.0, 2.0, 1, 1.0, 'url_imagen', '2025-06-02', 'available', TRUE),
('p2', 'u2', 'Casa a estrenar', 'Barrio residencial, cochera para dos vehículos', 'house', 'both', 10000000, 'Buenos Aires', 100.0, 7.5, 3, 2.5, 'url_imagen2', '2025-06-03', 'available', TRUE);


INSERT INTO Address (address_id, publication_id, street, number, letter, floor, neighborhood)
VALUES 
('a1', 'p1', 'Calle Falsa', 123, 'A', 2, 'Palermo'),
('a2', 'p2', 'Calle No tan Falsa', 123, null, null, 'Caballito');

-- Inserts para la tabla Conversation
INSERT INTO Conversation (conversation_id, tenant_id, landlord_id, publication_id, start_date, enabled) VALUES
('c11', 'u1', 'u2', 'p1', '2025-05-01', TRUE),
('c12', 'u1', 'u2', 'p2', '2025-05-05', TRUE),
('c13', 'u3', 'u2', 'p2', '2025-05-05', TRUE);

-- Inserts para la tabla Message
INSERT INTO Message (message_id, sender_id, receiver_id, conversation_id, content, date) VALUES
('m0001', 'u1', 'u2', 'c11', 'Hola, estoy interesado en la propiedad.', '2025-05-01'),
('m0002', 'u2', 'u1', 'c11', 'Hola, gracias por tu interés. Se estará mostrando lunes 16hs.', '2025-05-02'),
('m0003', 'u1', 'u2', 'c12', '¿Está disponible la publicación todavía?', '2025-05-05'),
('m0004', 'u2', 'u1', 'c12', 'Sí, sigue disponible.', '2025-05-06'),
('m0005', 'u3', 'u2', 'c13', '¿Podrías darme más detalles sobre la ubicación?', '2025-05-10');


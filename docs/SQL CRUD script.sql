USE nodo_inmobiliario;

#Registro de usuario nuevo
INSERT INTO user (user_id, name, surname, email, password, role, register_date, enabled)
VALUES ('123e4567', 'Santiago', 'Perez', 'santiago1@email.com', 'santiagopassword123', 'TENANT', '2025-06-05', true);

#Búsqueda de todos los users. Por regla de negocio se muestran solo activos.
SELECT user_id, name, surname, email, role
FROM user
WHERE enabled = TRUE;

#Búsqueda de user por rol. Por regla de negocio se muestran solo activos.
#Se ordena descendente por fecha de registro.
SELECT user_id, name, surname, email, role
FROM user
WHERE role = 'LANDLORD' AND enabled = TRUE
ORDER BY register_date DESC;

#Edición de user. Cambio de campo email.
UPDATE user
SET email = 'santiago2@email.com'
WHERE user_id = '123e4567';

#Creación de publicación asociada al usuario '123e4567';
INSERT INTO Publication 
VALUES (
    'Asd684ÑLk', '123e4567', 'Departamento céntrico',
    'Departamento de 2 ambientes en pleno centro',
    'Appartment', 'Rent', 120000, 'Buenos Aires', 65.5, 1, 1, 1.0,
    'https://depto.com/foto1.jpg', '2025-06-05', 'Available', TRUE
);

#Búsqueda de todas las publicaciones. Por regla de negocio, se traen solo las activas.
SELECT * FROM Publication
WHERE user_id = '123e4567'
AND enabled = true;

#Buscar una determinada publicación.
SELECT * FROM Publication
WHERE publication_id = 'Asd684ÑLk';

#Editar la publicación para cambiar el precio y descripción.
UPDATE Publication
SET price = 130000, publication_description = 'Departamento actualizado con cocina renovada'
WHERE publication_id = 'Asd684ÑLk';

#Eliminación lógica (ocultación) de la publicación. Preferible en caso de auditoría.
UPDATE Publication
SET enabled = false
WHERE publication_id = 'Asd684ÑLk';

#Borrado físico de la publicación.
DELETE FROM Publication
WHERE publication_id = 'Asd684ÑLk';

#Eliminación lógica de user (enabled pasa a false, no aparece en búsquedas
#pero es recuperable en caso de auditorías -preferible-).
UPDATE user
SET enabled = FALSE
WHERE user_id = '123e4567';

#Eliminación física de user (borrado de la base de datos).
DELETE FROM user
WHERE user_id = '123e4567';
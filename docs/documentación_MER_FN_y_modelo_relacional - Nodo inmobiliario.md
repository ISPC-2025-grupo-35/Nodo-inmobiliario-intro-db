#Documentación del modelo entidad-relación y del modelo relacional

##Descripción del Modelo Entidad-Relación (MER) de Chen

###Entidades y atributos:

* User: Representa a los usuarios del sistema (inquilinos, propietarios, etc.). Atributos: user_id, name, surname, email, password, role, register_date, enabled.

* Publication: Representan las distintas propiedades. Atributos: publication_id, user_id, title, description, type, operation, price, city, status, sqr_mts, spaces, bedrooms, bathrooms, picture_url, registered_state, enabled.

* Address: Dirección física asociada a una publicación. Atributos: address_id, publication_id, street, number, floor, letter, neighborhood.

* Conversation. Representa una conversación entre dos usuarios sobre una publicación. Atributos: conversation_id, publication_id, tenant_id, landlord_id, start_date, enabled.

* Message. Mensajes dentro de una conversación. Atributos: message_id, conversation_id, sender_id, receiver_id, content, date.


###Relaciones:

* makes (user — publication):
 Un usuario puede hacer muchas publicaciones (relación 1:N). Cada publicación pertenece a un solo usuario (participación 1).  Además, una publicación no puede existir sin un usuario (participación total en user del lado de publication).

* contains (publication — address): Una publicación tiene una sola dirección y viceversa, una dirección corresponde a una sola publicación (relación 1:1).  Ambas entidades tienen participación total en la relación: ninguna existe sin la otra.

* contains (publication — conversation): Una publicación puede tener varias conversaciones (relación 1:N). Cada conversación está asociada a una única publicación (participación 1). Una conversación no puede existir sin su publicación (participación total del lado de conversation).

* has (conversation — message):  Una conversación contiene muchos mensajes (relación 1:N).  Cada mensaje pertenece a una única conversación.  El mensaje no puede existir sin su conversación (participación total del lado de message).



##Transformación al modelo relacional y formas normales:

###1FN: 

- Cada entidad (User, Publication, Address, Conversation, Message) se convirtió en una tabla.

- Cada entidad tenía un atributo identificador (*_id) ya desde MER, estos fueron usados como clave primaria en el modelo relacional. 

- Si bien no había atributos multivaluados en el MER, se aseguró que todos los atributos del modelo relacional fueran atómicos (ej. street, number, email, date, etc.), lo que significa que no posean valores multivaluados o compuestos.

###2FN: 

- Las relaciones 1:N del MER (makes, contains, has) se resolvieron incorporando claves foráneas en el modelo relacional. Al no haber relaciones M:N, no hubo necesidad de convertir las relaciones del MER en entidades (tablas intermedias) del modelo relacional. 
Por otro lado, se agregaron otras claves foráneas necesarias no presentes en MER.

-> publication.user_id proviene de la relación makes entre User y Publication.
-> address.publication_id proviene de contains entre Publication y Address (1:1).
-> conversation.publication_id proviene de contains entre publicación y conversación.
-> conversation.tenant_id y conversation.landlord_id se crearon para relacionar cada publicación con dos entidades distintas de User (ambas necesarias para conversación).
-> message.conversation_id proviene de has entre Conversation y Message.
-> message.sender_id y message.receiver_id se crearon para relacionar cada mensaje con dos entidades distintas de User (ambas necesarias para el mensaje, para poder diferir claramente emisor y receptor a la hora de mostrarlos).

-Además, al tratarse de claves primarias simples (*_id, no compuestas), la condición necesaria de dependencia completa entre los atributos no clave y las claves primarias de las tablas se cumplió automáticamente.

###FN3:

- Si bien no se percibieron riesgos de dependencias transitivas, se optó para generar enums (Role_enum, Operation_enum, Property_type_enum, Status_enum) para evitar de antemano que cualquier valor que en el futuro pudiera asociarse exclusivamente a ellos debiera ser incorrectamente incluido como campo en las tablas que contenían esos enum (User para el primero, Publication para los otros tres).


##Descripción del modelo relacional:

* Tabla: user
Campos:
- user_id: VARCHAR(36), clave primaria, no nulo, único.
- name: VARCHAR(100), no nulo.
- surname: VARCHAR(100), no nulo.
- email: VARCHAR(100), no nulo, único (no se puede repetir).
- password: VARCHAR(255), no nulo.
- role: VARCHAR(50), clave foránea a role_enum(name), no nulo (participación obligatoria, todo usuario debe tener un rol asignado -y solo uno-). Relación N:1 desde user a role_user. Relación 0:N a la inversa (participación opcional, pueden existir registros de role_enum sin aplicarse a ninguna instancia de user, ej: que no haya usuario asignado como ADMIN; Así como debe ser posible que el mismo valor de role_enum sea asignado a múltiples instancias de user, ej: que haya múltiples TENANT -inquilinos-).
- register_date: DATE, no nulo.
- enabled: BOOL, no nulo.

* Tabla: role_enum
Campos:
-name: VARCHAR(50), clave primaria, no nulo, único.

* Tabla: publication
Campos:
-publication_id: VARCHAR(36), clave primaria, no nulo, único.
-user_id: VARCHAR(36), clave foránea a user(user_id), no nulo (participación obligatoria, toda publicación debe tener un autor -y solo uno-). Relación N:1 desde publication a user. Relación 0:N a la inversa (participación opcional, pueden existir registros de user que no realicen publicaciones, ej: los inquilinos no van a publicar propiedades; así como debe ser posible que un mismo usuario realice varias publicaciones, ej: un dueño puede tener varias propiedades para publicar).
-title: VARCHAR(255), no nulo.
-publication_description: TEXT, no nulo.
-property_type: VARCHAR(50), clave foránea a property_type_enum(name), no nulo (participación obligatoria, toda publicación debe aclarar el tipo de propiedad -solo una-). Relación N:1 desde publication a property_type. Relación 0:N a la inversa (participación opcional, pueden existir registros de property_type sin aplicarse a ninguna instancia de propiedad, ej: puede no haber propiedades del tipo CABAIN -cabaña- en la app; así como debe ser posible que el mismo valor de property_type sea asignado a múltiples instancias de propiedad, ej: seguramente más de una propiedad sea del tipo APPARTMENT -departamento-).
-operation: VARCHAR(50), clave foránea a operation_enum(name), no nulo (participación obligatoria, toda publicación debe aclarar qué operaciones permite -y solo un tipo-). Relación N:1 desde publication a operation_enum. Relación 0:N a la inversa (participación opcional, pueden existir registros de operation_enum sin aplicarse a ninguna instancia de propiedad, ej: puede que ninguna propiedad sea marcada BOTH, esto es, disponible a la vez para alquiler y venta; así como debe ser posible que el mismo valor de operation_enum sea asignado a múltiples instancias de propiedad, ej: varias propiedades serán asignadas para RENT -alquiler-).
-price: INT, no nulo.
-city: VARCHAR(100), no nulo.
-sqr_mts: FLOAT, no nulo.
-spaces: FLOAT, porque puede haber habitaciones demasiado pequeñas para ser legalmente consideradas dormitorios y además deben contarse los baños de servicio, no nulo.
-bedrooms: INT, no nulo.
-bathroom: FLOAT, porque puede haber baños de servicio, es decir, que no tengan ducha/bañera, no nulo.
-picture_url: VARCHAR(255), no nulo. De momento, se prefirió incluir una sola imagen y que esta sea obligatoria.
-register_state: DATE, no nulo.
-property_status: VARCHAR(50), clave foránea a status_enum(name), no nulo (participación obligatoria, toda publicación debe aclarar su status -y solo uno-). Relación N:1 desde publication a operation_enum. Relación 0:N a la inversa (participación opcional, pueden existir registros de status_enum sin aplicarse a ninguna instancia de propiedad, ej: puede que ninguna propiedad sea marcada OTM, esto es, fuera del mercado; así como debe ser posible que el mismo valor de status_enum sea asignado a múltiples instancias de propiedad, ej: varias propiedades serán asignadas AVAILABLE -disponibles-).
-enabled: BOOL, no nulo.

* Tabla: property_type_enum
Campos:
- name: VARCHAR(50), clave primaria, no nulo, único.

* Tabla: operation_enum
Campos:
- name: VARCHAR(50), clave primaria, no nulo, único.

* Tabla: status_enum
Campos:
- name: VARCHAR(50), clave primaria, no nulo, único.

* Tabla: address
Campos:
- address_id: VARCHAR(36), clave primaria, no nulo, único.
- publication_id: VARCHAR(36), clave foránea a publication(publication_id), no nulo (participación obligatoria, toda publicación debe estar asociada a una dirección), con restricción de unicidad (relación 1:1): toda propiedad (es decir, toda publicación) tendrá una dirección física, y una dirección física corresponde exactamente a solo una propiedad.
- street: VARCHAR(100), no nulo.
- number: INT, no nulo.
- letter: CHAR(1), nulo permitido.
- floor: INT, nulo permitido.
- neighborhood: VARCHAR(100), no nulo.

* Tabla: conversation
Campos:
- conversation_id: VARCHAR(36), clave primaria, no nulo, único.
- tenant_id: VARCHAR(36), clave foránea a user(user_id), no nulo (participación obligatoria, toda conversación debe incluir un inquilino que la inicie -y solo uno-). Relación N:1 desde conversation a user. A la inversa es 0:N, participación opcional, ya que puede existir un inquilino que no haya iniciado conversaciones, así como seguramente haya casos donde el inquilino participe en varias.
- landlord_id: VARCHAR(36), clave foránea a user(user_id), no nulo (participación obligatoria, toda conversación debe incluir un dueño que participe -y solo uno-). Igual al anterior, relación N:1 desde conversation a user, ya que toda conversación debe tener un inquilino que la inicie. A la inversa es 0:N, participación opcional, ya que puede existir un dueño que no haya recibido conversaciones, así como seguramente haya casos donde el dueño participe en varias.
- publication_id: VARCHAR(36), clave foránea a publication(publication_id), no nulo (participación obligatoria, toda conversación debe referir a una publicación -y solo una-). Relación N:1 desde conversation a publication. A la inversa, relación 0:N, pues puede que haya publicaciones que no tengan conversaciones iniciadas al respecto, así como otras publicaciones pueden tener iniciadas varias conversaciones.
- start_date: DATE, no nulo.
- enabled: BOOL, no nulo.

* Tabla: message
Campos:
- message_id: VARCHAR(36), clave primaria, no nulo, único.
- sender_id: VARCHAR(36), clave foránea a user(user_id), no nulo (participación obligatoria, todo mensaje debe tener un emisor -y solo uno-). Relación N:1 desde mensaje a user, ya que solo un usuario será el autor de cada mensaje. A la inversa, relación 0:N, ya que un usuario puede no haber enviado mensajes, o haber enviado múltiples.
- receiver_id: VARCHAR(36), clave foránea a user(user_id), no nulo (participación obligatoria, todo mensaje debe tener un receptor -y solo uno-). Igual a la anterior, relación N:1 desde mensaje a user. A la inversa, relación 0:N, ya que un usuario puede no haber recibido mensajes, o haber recibido múltiples.
- conversation_id: VARCHAR(36), clave foránea a conversation(conversation_id), no nulo (participación obligatoria, todo mensaje debe ser parte de una conversación -y solo una-). Relación N:1 desde mensaje a conversación. A la inversa, relación 1:N, ya que la conversación puede incluir múltiples mensajes, pero para existir debe al menos incluir uno.
- content: TEXT, no nulo.
- date: DATE, no nulo.

###Otras consideraciones: 
1. El equipo de desarrollo optó por mantener una nomenclatura de las tablas en snake_case y singular. Se reconoce que la convención es snake_case y plural.

2. En las tablas correspondientes a Enums (role_enum, operation_enum, property_type_enum, status_enum) se optó porque el propio nombre fuera la clave primaria, ya que el mismo es suficientemente descriptivo y no debe repetirse bajo ningún concepto otro registro con el mismo valor en estas tablas. Si sucediera dicha repetición, estaría habiendo inconsistencia de datos o alguna irregularidad respecto a las reglas del negocio.

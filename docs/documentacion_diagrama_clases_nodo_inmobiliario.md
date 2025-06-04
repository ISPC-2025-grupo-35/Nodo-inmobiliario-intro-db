
# Generalidades

El diagrama de clases de Nodo Inmobiliario presenta 5 clases principales: `User`, `Publication`, `Address`, `Conversation` y `Message`. Todos los atributos de estas clases poseen modificador de acceso privado. Cabe destacar que 3 de las clases poseen un atributo booleano `enabled`, pensado para realizar eliminaciones lógicas —no físicas— cuando sea necesario. Las dos clases que no lo incluyen (`Address` y `Message`) carecen de sentido funcional si se eliminan las instancias de las cuales dependen (`Publication` y `Conversation`, respectivamente). Este tipo de dependencia se corresponde con una relación de composición, que será detallada más adelante.

Las clases `Role_enum`, `Property_type_enum`, `Operation_enum` y `Status_enum` son enumeraciones que no poseen atributos adicionales más allá de los valores predefinidos. Dado que su valor es suficiente para identificarlas en el contexto de uso, no requieren clave primaria.


# Clase `User`

La clase `User` representa a los usuarios de la app, independientemente de su rol. Posee una relación 1:1 con `User_role` (toda instancia de `User` debe tener un rol asignado al momento de la creación; no puede existir un usuario sin rol). A la inversa, `User_role` tiene una relación 0..* con `User`, ya que un rol puede existir sin estar asignado a ningún usuario y puede repetirse entre múltiples usuarios.

**Atributos:**
En detalle, la clase `User` posee los atributos `user_id: str`, `name: str`, `surname: str`, `email: str`, `password: str`, `role: Role_enum`, `register_date: Date` y `enabled: bool`. El `user_id` se autogenera (UUID), al igual que `register_date` (al momento de registrarse) y `enabled` (inicializado como `True`).

**Métodos:**
- `register()`: permite dar de alta una nueva instancia de `User`. Requiere `name`, `surname`, `email` y `role`, completando el resto de los atributos internamente (sin devolver la contraseña).
- `login()`: requiere `email` y `password`. Devuelve una instancia `User` si las credenciales coinciden.
- `get_user_by_id()`: pensado para uso administrativo, devuelve la instancia `User` si el ID está registrado y activo.
- `get_user_by_email()`: devuelve la instancia `User` si el email está registrado y activo.
- `get_all_users()`: devuelve todas las instancias `User` activas.
- `get_all_users_by_role()`: devuelve las instancias activas de `User` que posean el rol indicado.
- `update_user()`: permite editar `name`, `surname`, `email` y `password`, validando que el email coincida con el del usuario registrado. Devuelve la instancia actualizada (sin contraseña).
- `change_user_role()`: exclusivo para administradores. Modifica el rol de una instancia `User` indicada por `user_id`. Devuelve `True` o `False` según éxito.
- `delete_user()`: desactiva lógicamente al usuario (`enabled = False`) validando su email. Devuelve `True` o `False`.



**Para el presente MVP, se desarrollan `User` y `Role_enum`. Las clases siguientes se consideran parte de entregas futuras.**



# Clase `Publication`

La clase `Publication` representa propiedades que los usuarios publican en la plataforma para alquiler o venta. Es central en el modelo y se relaciona con múltiples entidades.

Al igual que en `User`, los enums relacionados (`Property_type_enum`, `Operation_enum`, `Status_enum`) están en relación 1:1 desde la perspectiva de `Publication`: cada instancia debe tener un valor definido de cada uno. A la inversa, cada enum puede no estar aún asignado a ninguna publicación y puede reutilizarse (relación 0..*).

En relación con `User`, `Publication` está compuesta por el usuario que la crea (rol `Landlord`). Si un usuario se retira de la app, sus publicaciones pierden sentido de negocio, por lo tanto esta es una relación de composición 1:N. Múltiples publicaciones pueden pertenecer al mismo usuario, pero cada una de ellas solo tiene un único usuario asociado.

`Publication` también tiene una relación de composición 1:1 con `Address`, ya que la dirección física carece de sentido sin la publicación asociada, y solo puede (y debe) haber una dirección para cada inmueble, y viceversa.

En cuanto a `Conversation`, una publicación puede estar asociada a múltiples conversaciones. Cada conversación está ligada a una publicación específica. Aunque el diseño actual no lo impone estructuralmente, se espera desde el comportamiento del sistema que exista solo una conversación activa entre un inquilino y un propietario por cada publicación. Este criterio deberá implementarse a nivel lógico o de control de aplicación.

**Atributos:**
- `publication_id: str`, `user_id: str`, `title: str`, `description: str`, `type: Property_type_enum`, `operation: Operation_enum`, `price: int`, `address: Address`, `city: str`, `sqr_mts: float`, `spaces: float` (no int, es posible que haya habitaciones demasiado pequeñas para ser legalmente consideradas dormitorios o caso de baños de servicio, que se marcan como '.5' en el conteo), `bedrooms: int`, `bathroom: float` ('.5 para baños de servicio, sin ducha/bañera), `picture_url: str` (inicialmente, solo una imagen por publicación), `register_date: Date`, `status: Status_enum`, `enabled: bool`.

**Métodos:**
- `create_publication()`: recibe los parámetros (excepto `publication_id`, `register_date`, `enabled`) y devuelve `True` o una instancia, según se defina más útil durante la implementación.
- `get_publication_by_id()`: devuelve la publicación asociada al id provisto, si es que esta existe (esté activa o no).
- `get_all_publications()`: devuelve las publicaciones activas (`enabled == True`).
- `get_all_publications_by_user_id()`: devuelve todas las publicaciones (activas o no) creadas por un usuario con rol `Landlord`. Debe incluir dicha validación.
- `update_publication()`: actualiza los datos de la publicación excepto `publication_id`, `enabled`, `status` y `register_date`. Devuelve la instancia modificada.
- `update_status()`: cambia el estado de disponibilidad (`status`) de una publicación. No equivale a desactivarla. Devuelve `True` si tuvo éxito.
- `delete_publication()`: baja lógica (`enabled = False`) de la publicación. Devuelve `True` si tuvo éxito.


# Clase `Address`

Representa la dirección física asociada a una publicación.

**Atributos:**
- `address_id: str`, `publication_id: str`, `street: str`, `number: int`, `letter: str`, `floor: int`, `neighborhood: str`.

**Métodos:**
- `create_address()`: requiere los datos mencionados (excepto `address_id`). Devuelve `True` si se crea correctamente. Debe poder recibir valores nulos en letter, floor y neighborhood, dada las diferentes formas de nomenclatura de las direcciones según zona, tipo de inmueble, etc.
- `get_address_by_publication_id()`: busca una instancia `Address` por ID de publicación que se le indica. La muestra si existe y está disponible.
- `update_address()`: actualiza los datos de una dirección existente. No se modifica `address_id`. Devuelve la instancia modificada.

Esta clase podría ampliarse en el futuro para incluir visualización de ubicación en mapas mediante integración con APIs externas.


# Clase `Conversation`

Representa el intercambio entre un `Tenant` y un `Landlord` acerca de una publicación específica. Está ligada por composición tanto a `Publication` como a dos instancias distintas de `User`. Cada user puede tener de 0 a múltiples conversaciones (0..*), pero cada conversación puede y debe tener solo un user de cada rol -representado con las dos flechas de composición entre User y Conversation-. 

Además, contiene una relación 1:N con `Message`, ya que una conversación puede tener múltiples mensajes asociados (de hecho, debe tener al menos uno para iniciarse, esto es 1..*), pero cada mensaje pertenece a una sola conversación.

**Atributos:**
- `conversation_id: str`, `tenant_id: str`, `landlord_id: str`, `publication_id: str`, `start_date: Date`, `enabled: bool`.

**Métodos:**
- `create_conversation()`: requiere los tres IDs (`tenant_id`, `landlord_id`, `publication_id`) y el mensaje inicial. Crea y devuelve la nueva conversación, autogenerando conversation_id (uuid), start_date y enabled (True).
- `get_conversation_by_id()`: requiere un conversation_id, devuelve la conversación correspondiente si existe.
- `get_all_conversations_by_user()`: requiere user_id, devuelve todas las conversaciones en las que participa un usuario determinado. Debe funcionar como un historial de mensajes, tanto para tenant como para landlord.
- `get_all_conversations_by_publication()`: requiere landlord_id y conversation_id, ya que está pensado exclusivamente para `Landlord`, devuelve todas las conversaciones asociadas a una publicación dada. Para tenant no tendría sentido, puesto que, por publicación, solo tendrá una conversación.
- `disable_conversation()`: baja lógica de la conversación (`enabled = False`), oculta las mismas a los usuarios pero queda disponible en caso de auditoría.


# Clase `Message`

Cada mensaje forma parte de una conversación y representa el contenido enviado entre dos usuarios.

**Atributos:**
- `message_id: str`, `sender_id: str`, `receiver_id: str`, `conversation_id: str`, `content: str`, `date: Date`.

**Métodos:**
- `send_message()`: requiere `conversation_id`, `sender_id` y `content`. Los campos restantes (`message_id`, `receiver_id`, `date`) se completan automáticamente. Devuelve una nueva instancia `Message`.


# Enums

- **`Role_enum`**: `ADMIN`, `LANDLORD`, `TENANT`
- **`Property_type_enum`**: `HOUSE`, `APPARTMENT`, `STUDIO`, `DUPLEX`, `CABAIN`
- **`Operation_enum`**: `RENT`, `PURCHASE`, `BOTH`
- **`Status_enum`**: `AVAILABLE`, `PAUSED`, `OTM` (Off the Market – fuera del mercado)

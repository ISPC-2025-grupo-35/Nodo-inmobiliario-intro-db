#Evidencia 3. Aportes al proyecto. 


##Guillermo Diván realizó: 
Creación y documentación del diagrama de clases.
Creación de User class y User_role enum (models).
Creación de métodos register(), update(), change_role() (only admin), login() y disable_account() en service y repository.
Consultas creación de database sql script y carga de datos.
Creación y documentación del Modelo relacional y formas normales. 
Documentación del modelo entidad-relación (Chen).

##Santiago Terragni realizó:
Modelo entidad-relación (Chen).

##Guillermo y Santiago realizaron en conjunto (pair programming):
Arquitectura en capas (models, views, services, repositories).
Creación del menú (view).
Validaciones.
Creación de métodos de lectura: get_user_by_email(), get_user_by_id() (only Admin), get_all_users(), get_all_users_by_role(); en service y repository. Se definió traer solo los usuarios activos (enabled == True) para emular el eliminado lógico.
Consultas CRUD sql script.



###Notas generales: 
* El array que emula la persistencia de datos del programa inicia con un usuario ya cargado. email: pedropascal@gmail, password pedro123.
* En el script de consultas CRUD sql, se decidió dejar al final las eliminaciones lógicas y físicas de usuario y publicación, para que el mismo no arrojara error si se ejecutaba al completo. Desde ya, si se ejecuta todo el script de una vez, no se apreciarán cambios (porque se borrarán los registros).
* Si bien se detalla en todo lugar que corresponda, se priorizó la eliminación lógica (updates a enabled = false cuando se quisiera eliminar), ocultando estas instancias en las búsquedas, para mantener la integridad de datos y conservar debido registro de la información en caso de auditorías.

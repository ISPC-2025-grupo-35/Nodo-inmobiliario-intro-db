from services.User_service import UserService
from models.User import User
from models.User_role import RoleEnum

user_service = UserService()
current_user = None

def menu():
    while True:
        option = input("Elija una opción: 1. registrarse. " \
        "2. ingresar a la app. 3. ver listado de usuarios. "
        "4. ver listado de usuarios por rol. 5. buscar usuario por id."
        "6. buscar usuario por email. 7. editar datos de usuario."
        "8. eliminar la cuenta. 9. cambiar rol de usuario."
        "0. Salir.")
        if option == "1":
            user_service.register()
        elif option == "2":
            current_user = user_service.login()
        elif option == "3":
            user_service.get_all_users()
        elif option == "4":
            user_service.get_users_by_role()
        elif option == "5":
            if current_user != None and current_user.role == RoleEnum.ADMIN:
                user_service.get_user_by_id()
        elif option == "6":
            user_service.get_user_by_email()
        elif option == "7":
            user_service.edit_self()
        elif option == "8":
            user_service.deactivate_self()
        elif option == "9":
            if current_user != None and current_user.role == RoleEnum.ADMIN:
                user_service.change_user_role()
        elif option == "0":
            print("Saliendo de Nodo Inmobiliario...")
            break
        else:
            print("Opción no válida. Vuelva a intentar.\n")
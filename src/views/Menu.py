from services.User_service import UserService
from models.User import User
from models.Role_enum import RoleEnum

class Menu():
    
    def __init__(self, service: UserService):
            self.__service = service
            self.current_user = None

    def run_menu(self):
        while True:
            if (self.current_user != None):
                print(f"Usuario conectado: {self.current_user.email}")
            option = input("Elija una opción: \n1. Registrarse. \n" \
            "2. Ingresar a la app. \n3. Ver listado de usuarios. \n"
            "4. Ver listado de usuarios por rol. \n5. Buscar usuario por id. \n"
            "6. Buscar usuario por email. \n7. Editar datos de usuario. \n"
            "8. Cambiar rol de usuario. \n9. Eliminar la cuenta. \n"
            "0. Salir. \n")
            if option == "1":
                name = input("Ingrese su nombre: ")
                surname = input("Ingrese su apellido: ")
                email = input("Ingrese su email: ")
                password = input("Ingrese su contraseña. " \
                "Recuerde que debe tener mínimo 6 caracteres e incluir números y letras: ")
                repeat_password = input("Ingrese nuevamente su contraseña.")
                if (password != repeat_password):
                    print("Las contraseñas no coinciden. Vuelva a registrarse")
                    continue
                role = None
                roleInput = input("Ingrese su rol. 1) Inquilino. 2) Dueño. 3) Admin: ")
                match(roleInput):
                    case "1": role = RoleEnum.TENANT
                    case "2": role = RoleEnum.LANDLORD
                    case "3": role = RoleEnum.ADMIN
                    case _: print("Rol no reconocido. Ingrese un rol válido. \n")
                created_user = self.__service.register(name=name, surname=surname, email=email,
                     password=password, role=role)
                if (created_user):
                    print("Usuario creado exitosamente. Puede proceder a iniciar sesión.")

            elif option == "2":
                email = input("Ingrese su email.")
                password = input("Ingrese su contraseña.")
                self.current_user = self.__service.login(email, password)

            elif option == "3":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                data = self.__service.get_all_users()
                print(f"Lista de usuarios activos: {data} \n")
                
            elif option == "4":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                role = None
                while (role == None):
                    roleInput = input("Ingrese el rol buscado. 1) Inquilino. 2) Dueño. 3) Admin: ")
                    match(roleInput):
                        case "1": role = RoleEnum.TENANT
                        case "2": role = RoleEnum.LANDLORD
                        case "3": role = RoleEnum.ADMIN
                        case _: print("Rol no reconocido. Ingrese un rol válido.")
                data = self.__service.get_all_users_by_role(role)
                print(f"Lista de usuarios con rol seleccionado: {data} \n")

            elif option == "5":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                if (self.current_user.role != RoleEnum.ADMIN):
                    print("Error, acción solo accesible para admin!")
                    continue
                id = input("Ingrese el id del usuario que desea buscar.")
                user_found = self.__service.get_user_by_id(id)
                print(f"El usuario encontrado es: {user_found} \n")

            elif option == "6":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                email = input("Ingrese el email del usuario que desea buscar.")
                user_found = self.__service.get_user_by_email(email)
                if (user_found == None):
                    print("No se encontró el usuario buscado.")
                print(f"El usuario encontrado es: {user_found} \n")

            elif option == "7":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                input_email = input("Ingrese su dirección de " \
                "email para confirmar la modificación de la cuenta.")
                if self.current_user.email != input_email:
                    print("El email solicitado no coincide con el de la cuenta activa.")
                else:
                    print("Reingrese los valores para cada campo.")
                    name = input("Ingrese su nombre")
                    surname = input("Ingrese su apellido")
                    password = input("Ingrese su contraseña. " \
                    "Recuerde que debe tener mínimo 6 caracteres e incluir números y letras.")
                    updated_user = self.__service.update_user(name=name, surname=surname, 
                                                                 email=input_email, password=password)
                    if (updated_user):
                        print(f"Usuario modificado exitosamente!  {updated_user} \n") 

            elif option == "8":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                if (self.current_user.role != RoleEnum.ADMIN):
                    print("Error, acción solo accesible para admin!")
                    continue
                role = None
                while (role == None):
                    roleInput = input("Ingrese el nuevo rol. 1) Inquilino. 2) Dueño. 3) Admin.")
                    match(roleInput):
                        case "1": role = RoleEnum.TENANT
                        case "2": role = RoleEnum.LANDLORD
                        case "3": role = RoleEnum.ADMIN
                        case _: print("Rol no reconocido. Ingrese un rol válido.")
                user_id = input("Ingrese el id del usuario para modificarle el rol")
                self.__service.change_user_role(user_id, role)

            elif option == "9":
                if (self.current_user == None):
                    print("Error, debe iniciar sesión primero!")
                    continue
                input_email = input("Ingrese su dirección de " \
                "email para confirmar la baja de la cuenta.")
                if self.current_user.email != input_email:
                    print("El email solicitado no coincide con el de la cuenta activa.")
                else:
                    disabled_user = self.__service.disable_account(input_email)
                    if (disabled_user):
                        self.current_user = None
                        print("La cuenta se eliminó exitosamente. Presione 0 para salir "
                        "o presione 2 para ingresar con otra cuenta.")

            elif option == "0":
                print("Saliendo de Nodo Inmobiliario...")
                break
            
            else:
                print("Opción no válida. Vuelva a intentar.\n")


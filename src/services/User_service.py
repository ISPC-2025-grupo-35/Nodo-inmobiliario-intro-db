from models.User import User
from models.Role_enum import RoleEnum
from repositories.User_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def register(self, name: str, surname: str, email: str,
                 password: str, role: RoleEnum) -> User:
        if not all([name, surname, email, password]):
            print("Error! No se permiten campos vacíos. \n")
            return None

        already_exists = self.get_user_by_email(email)
        if already_exists:
            print("Error! Este usuario ya se encuentra registrado! Proceda a iniciar sesión. \n")
            return None

        if len(password) < 6 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            print("Contraseña inválida. Recuerde que debe tener" \
            " longitud de 6 caracteres mínimo e incluir letras y números. \n")
            return None
        
        created_user = User(name, surname, email, password, role)

        self.__repository.register_user(created_user)

        return created_user
        
    def login(self, user_email: str, password: str) -> User:
        data = self.get_user_by_email(user_email)
        if data is None:
            return None
        if data.password == password:
            print(f"Acceso permitido! Hola {data.name}! \n")
            return data
        else:
            print("Acceso denegado, contraseña incorrecta. \n")
            return None

    #Solo para ADMIN.
    def get_user_by_id(self, user_id: str) -> 'User':
        user = self.__repository.get_user_by_id(user_id)
        if user is None:
            print("No se encontró el usuario buscado. \n")
            return None
        return user

    #Solo para USER (entrega ev3, lógica de negocio distinta).
    def get_user_by_email(self, user_email: str) -> 'User':
        user = self.__repository.get_user_by_email(user_email)
        if user is None:
            return None
        return user
    
    def get_all_users(self) -> list['User']:
        users = self.__repository.get_all_users()
        return users

    def get_all_users_by_role(self, role: RoleEnum) -> list['User']:
        users = self.__repository.get_all_users_by_role(role)
        return users

    def update_user(self, name: str, surname: str, 
                       email: str, password: str) -> 'User':
        
        if not all([name, surname, email, password]):
            print("Error! No se permiten campos vacíos. \n")
            return None

        if len(password) < 6 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            print("Contraseña inválida. Recuerde que debe tener" \
            "longitud de 6 caracteres mínimo e incluir letras y números. \n")
            return None
        
        user = self.__repository.update_user(name=name, surname=surname,
                                      password=password, email=email)

        return user

    #Solo para admin
    def change_user_role(self, user_id: str, role: RoleEnum) -> bool:
        searched_user = self.get_user_by_id(user_id)
        if searched_user is None:
            return False
        self.__repository.change_user_role(user_id, role)
        return True

    def disable_account(self, user_email: str) -> bool:
        self.__repository.disable_account(user_email)
        return True

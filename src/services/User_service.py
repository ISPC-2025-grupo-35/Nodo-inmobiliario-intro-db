from models.User import User
from models.User_role import RoleEnum
from repositories.User_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def register(self, name: str, surname: str, email: str,
                 password: str, role: RoleEnum) -> User:
        if not all([name, surname, email, password]) or not RoleEnum.has(role):
            print("Mensaje sobre campos vacíos o rol mal escrito")
            return None

        already_exists = self.get_user_by_email(email)
        if already_exists:
            print("Mensaje sobre usuario ya existiendo")
            return None

        if len(password) < 6 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            print("Password must be at least 6 characters long and contain both letters and numbers.")
            return None
        
        created_user = User(name, surname, email, password, role)

        self.__repository.register_user(created_user)

        return created_user
        
    def login(self, email: str, password: str) -> User:
        '''
        TODO: IMPLEMENTAR!
        Debe recibir email y password.
        Corroborar contra array (O base de datos...)
        y devolver bool según lo encuentre o no.
        Desde el menú se procede a informar si hubo éxito o no en el login.
        '''
        return None

    #Ponerlo solamente para ADMIN.
    def get_user_by_id(self, user_id: str) -> 'User':
        data = UserRepository().get_user_by_id(user_id)
        if data is None:
            print("No se encontró el usuario buscado")
            return None
        user = User(data[1], data[2], data[3], data[4], data[5],)
        user.user_id = data[0]
        user._register_date = data[6]
        user.enabled = data[7]
        return user

    def get_user_by_email(self, user_email: str) -> 'User':
        data = UserRepository().get_user_by_email(user_email)
        if data is None:
            return None
        user = User(data[1], data[2], data[3], data[4], data[5], )
        user.user_id = data[0]
        user._register_date = data[6]
        user.enabled = data[7]
        return user 

    def get_all_users(self) -> list['User']:
        '''
        Idéntico al get_all_users_by_role pero sacar filtro de rol.
        '''
        pass

    def get_all_users_by_role(self, role: RoleEnum) -> list['User']:
        if not RoleEnum.has(role):
            print("El rol asignado está mal escrito")
            return None
        repository = UserRepository().get_all_users_by_role(role)
        users = list(repository)
        return users

    def update_profile(self, user_id: str, updated_user: 'User') -> 'User':
        '''
        Debe recibir user_id y User con parámetros para que lo reciba 
        el correspondiente constructor (ver clase User).
        Buscar el user by id (llamar al método ya creado)
        Asignar los nuevos valores del updated_user. 
        Agregar ANTES DE LA BÚSQUEDA corroboración de que sí exista...
        (ver email_exists en register!)
        '''
        pass

    #Ponerlo solamente para ADMIN.
    def change_user_role(self, user_id: str, role: RoleEnum) -> bool:
        if not RoleEnum.has(role):
            print("El rol asignado está mal escrito")
            return False
        searched_user = self.get_user_by_id(user_id)
        if searched_user is None:
            return False
        self.__repository.change_user_role(user_id, role)
        return True

    def disable_account(self, user_email: str) -> bool:
        '''
        TODO: IMPLEMENTAR!
        Debe recibir email.
        Debe corroborar que el email logueado y el dado sean el mismo 
        (desde el menú!)
        Debe pasar el enabled al opuesto.
        Devolver el valor de enabled. 
        '''
        pass

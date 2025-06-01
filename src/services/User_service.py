from models.User import User
from models.User_role import RoleEnum

class UserService:
    def __init__(self):
        self._users = []

    def register(self, name: str, surname: str, email: str,
                 password: str, role: RoleEnum) -> bool:
        if (not name or not surname or not email or not password 
            or not RoleEnum.has(role)):
            return False
        email_exists = any(filter(lambda u: u.email == email, self._users))
        if email_exists:
            return False
        #TODO: AGREGAR VALIDACIÓN DE CONTRASEÑA.
        user = User(name, surname, email, password, role)
        self._users.append(user)
        return user

    def login(self, email: str, password: str) -> User:
        '''
        TODO: IMPLEMENTAR!
        Debe recibir email y password.
        Corroborar contra array (O base de datos...)
        y devolver bool según lo encuentre o no.
        Desde el menú se procede a informar si hubo éxito o no en el login.
        '''
        return None

    def get_user_by_id(self, user_id: str) -> 'User':
        user_exists = next(filter(lambda u: u.user_id == user_id, 
                                  self._users), None)
        return user_exists

    def get_user_by_email(self, user_email: str) -> 'User':
        '''
        Idéntico al get_user_by_id pero cambiar por user_email en lambda!
        '''
        pass

    def get_all_users(self) -> list['User']:
        '''
        Idéntico al get_all_users_by_role pero sacar filtro de rol.
        '''
        pass

    def get_all_users_by_role(self, role: RoleEnum) -> list['User']:
        users_by_role = list(filter(lambda u: u.role == role, self._users))
        return users_by_role

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

    def change_user_role(self, user_id: str, role: RoleEnum) -> bool:
        # Debe corroborar que el rol de admin desde desde el menú!
        searched_user = self.get_user_by_id(user_id)
        searched_user.role = role
        return searched_user.role
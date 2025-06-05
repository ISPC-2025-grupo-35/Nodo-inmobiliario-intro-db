from models.Role_enum import RoleEnum
from models.User import User

class UserRepository: 

    def __init__(self):
        mock_user = User("Pedro", "Pascal", "pedropascal@gmail.com", "pedro123", RoleEnum.ADMIN)
        self.__Users =[mock_user, ] 
        
    def register_user(self, created_user: User):
        self.__Users.append(created_user)
        return created_user

    def get_user_by_id(self, user_id: str):
        user_exists = next(filter(lambda u: u.user_id == user_id
                                  and u.enabled == True, 
                                  self.__Users), None)
        return user_exists
        
    
    def get_user_by_email(self, user_email: str):
        user_exists = next(filter(lambda u: u.email == user_email
                                  and u.enabled == True,  
                                  self.__Users), None)
        return user_exists

    def get_all_users(self):
        user_list = list(filter(lambda u: u.enabled == True, 
                                  self.__Users))
        return user_list

    def get_all_users_by_role(self, role: RoleEnum):
        user_list = list(filter(lambda u: u.enabled == True
                                  and u.role == role,
                                  self.__Users))
        return user_list
    
    def update_user(self, name: str, surname: str, email: str, password: str):
        searched_user = self.get_user_by_email(email)
        searched_user.name = name
        searched_user.surname = surname
        searched_user.password = password
        return searched_user
    
    def change_user_role(self, user_id: str, role: RoleEnum):
        searched_user = self.get_user_by_id(user_id)
        searched_user.role = role
        return searched_user

    def disable_account(self, user_email: str):
        searched_user = self.get_user_by_email(user_email)
        searched_user.enabled = False
        return searched_user
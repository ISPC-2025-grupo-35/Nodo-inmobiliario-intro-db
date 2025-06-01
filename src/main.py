from services.User_service import UserService
from repositories.User_repository import UserRepository
from models.User_role import RoleEnum

def main():
    us = UserService(UserRepository())
    #find_user_by_id = us.get_user_by_id('6e2f98ea-17c1-4e41-86a0-6f819d6203ac')
    #print(find_user_by_id)
    #find_users_by_role = us.get_all_users_by_role(RoleEnum.TENANT)
    #print(len(find_users_by_role))
    #find_user_by_email = us.get_user_by_email('lilili@lilili.com')
    #print(find_user_by_email)
    #new_user = us.register("Roberto", "Garcia", "robertogarcia2@gmail.com", "pepe1234", RoleEnum.TENANT)
    #print(new_user)
    #changed_role = us.change_user_role('6e2f98ea-17c1-4e41-86a0-6f819d6203ac', RoleEnum.LANDLORD)
    #print(changed_role)


if __name__ == "__main__":
    main()
from services.User_service import UserService
from models.User_role import RoleEnum

def main():
    us = UserService()
    new_user = us.register("Pepe", "Argento", "pepe@pepe.com", "pepe1234", RoleEnum.TENANT)
    print(new_user.user_id)
    find_user_by_id = us.get_user_by_id(new_user.user_id)
    print(find_user_by_id.user_id)
    find_users_by_role = us.get_all_users_by_role(RoleEnum.TENANT)
    print(len(find_users_by_role))
    change_user_role = us.change_user_role(new_user.user_id, RoleEnum.ADMIN)
    print(new_user.role)
    print(change_user_role)


if __name__ == "__main__":
    main()
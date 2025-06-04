from services.User_service import UserService
from repositories.User_repository import UserRepository
from views.Menu import Menu

def main():
    menu = Menu(UserService(UserRepository()))
    menu.run_menu()

if __name__ == "__main__":
    main()
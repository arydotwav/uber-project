from auth.auth_manager import AuthManager
from auth.user import Passanger, Driver
from core.controller import Controller

class TripUI:
    def __init__(self):
        self.user = None

    def start_trip(self, user):
        self.user = user
        print(f"🚗 Starting trip for {self.user.name} ({self.user.email})")

def main():
    auth = AuthManager()
    trip_ui = TripUI()
    controller = Controller()

    username = input("Username: ")
    password = input("Phone (used as password): ")

    if auth.login(username, password):
        user = auth.get_current_user()
        if isinstance(user, Passanger):
            trip_ui.start_trip(user)
            controller.confirm_trip()
        elif isinstance(user, Driver):
            show = input(("(Driver)Do you want to show as active?\n(y/n)"))
            if show == "y":
                controller = Controller()
                user.status = True
                controller.find_trip()
            else:
                print("You will stay as inactive.")
        
        option = input("Do you want to logout? (y/n): ").lower()
        if option == 'y':
            auth.logout()
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()

##va para el trip ui, el trip_ui es el que tiene que heredar el controller.
import time
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.trip_manager import TripManager
from ui.follow_up import FollowUp
from auth.user import Driver, Passanger
from core.controller import Controller
from auth.auth_manager import AuthManager

class TripUi(Controller):

    def login(self):
        auth = AuthManager()
        controller = Controller()

        username = input("Username: ")
        password = input("Phone (used as password): ")

        if auth.login(username, password):
            user = auth.get_current_user()
            if isinstance(user, Passanger):
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

    def __init__(self):
        self.logged_in= True
        self.username = "Pepe"
        self.tm = TripManager()
        self.active_driver = ""
        self.follow = FollowUp()

    def welcome(self):
        print("----  Uber  ----")
        time.sleep(1)
        return f" Hola {self.username}, a donde queres ir hoy? "
    
    def show_drivers(self):

        self.active_driver = self.tm.find_driver() or "No se encontro un conductor"

        return f"Conductores disponibles: {self.active_driver}"
    
    def trip_confirmed(self):
        print("To do")

    def show_driver_info(self):

        driver = Driver("Dardo", "1122668790", "dardito@mail.com", True)

        return f"""
        -----
        Informacion del conductor
        Nombre: {driver.name}
        Patente: {random.randint(1000,9000)}
        -----
        """
    
    def follow_up(self):

        self.follow.show_info()

    def start_trip(self):
        self.login()

trip = TripUi()

#print(trip.welcome())
trip.start_trip()
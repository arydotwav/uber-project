import time
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.trip_manager import TripManager
from ui.follow_up import FollowUp
from auth.user import Driver, Passenger
from core.controller import Controller
from auth.auth_manager import AuthManager

class TripUi(Controller):

    
    def __init__(self):

        self.username = None
        self.tm = TripManager()
        self.active_driver = ""
        self.follow: FollowUp = None
        
    def welcome(self):
        print("----  Uber  ----")
        time.sleep(1)
        print("Welcome! Please log in!")

    
    def login(self):
        auth = AuthManager()
        success = False
        username = input("Username: ")
        new_trip = 'y'
    
        while new_trip == 'y':
            if success == False:
                password = input("Phone (used as password): ")
            success = auth.login(username, password)


            if success:
                self.user = auth.get_current_user()

                if isinstance(self.user, Passenger):
                    driver = self.tm.confirm_trip()
                    print(f"Your driver is {driver}  TRIPUI CLASS")
                    # fix the infinite loop
                    self.follow = FollowUp(driver=driver)
                    self.follow.show_info()
                elif isinstance(self.user, Driver):
                    show = input("(Driver) Do you want to show as active?\n(y/n): ")
                    if show.lower() == "y":
                        self.user.status = True
                        self.tm.find_trip()
                    else:
                        print("You will stay as inactive.")

                option = input("Do you want to logout? (y/n): ").lower()
                if option == 'y':
                    auth.logout()
                    new_trip = 'no'
                elif option == 'n':
                    print("You will stay logged in.")
                    new_trip = input("Do you want to take another trip? (y/n)").lower()
                    
            else:
                print("❌ Login failed. Try again.\n")


        print("Closing the app.")
    
    # def trip_confirmed(self):
    #     print("To do")

    def start_trip(self):
        self.welcome()
        self.login() 

    # def show_driver_info(self):
    #     driver = Driver("Dardo", "1122668790", "dardito@mail.com", True)
    #     return f"""
    #     -----
    #     Informacion del conductor
    #     Nombre: {driver.name}
    #     Patente: {random.randint(1000,9000)}
    #     -----
    #     """
    
    # def follow_up(self):

    #     self.follow.show_info()

    # def show_drivers(self):
    #     self.active_driver = self.tm.find_driver() or "No se encontro un conductor"
    #     return f"Conductores disponibles: {self.active_driver}"


# trip = TripUi()

# #print(trip.welcome())

# print(trip.show_drivers())

# print(trip.show_driver_info())

# print(trip.follow_up())
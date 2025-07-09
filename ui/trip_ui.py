import time
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.trip_manager import TripManager

from ui.follow_up import FollowUp

from test.user import Driver

#Usar las demas clases para obtener los datos

class TripUi():

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
    
    def trip_confirmed():
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



trip = TripUi()

#print(trip.welcome())

print(trip.show_drivers())

print(trip.show_driver_info())

print(trip.follow_up())


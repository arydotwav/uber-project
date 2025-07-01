import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import time
from auth.auth_manager import AuthManager

class TripManager:
    def __init__(self):
        self.auth = AuthManager()
        self.available_drivers = self.auth.drivers
        self.available_trips = self.auth.passengers

    def confirm_trip(self):
        print("Finding a driver...")
        while True:
            time.sleep(1)  
            driver = self.find_driver()
            if driver.status:
                print(f"The driver {driver} is accepting the trip..")
                return f"Trip confirmed with {driver}"
            else:
                print("The driver rejected the trip.")

    def find_trip(self):
        while True:
            time.sleep(1)
            passenger = self.find_passenger()
            if passenger:
                print("Searching for a trip..")
                time.sleep(1)
                return f"Trip confirmed for {passenger.name} ({passenger.telephone})"
            else:
                print("No trips available.")
            
    def find_driver(self):
        return random.choice(self.available_drivers)

    def find_passenger(self):
        return random.choice(self.available_trips)

# trip1 = TripManager()
# print(trip1.find_trip())
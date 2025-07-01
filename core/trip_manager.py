import random
import time

class TripManager:
    def __init__(self):
        self.available_drivers = ["Varus","Valmar","Kai", "Gwen", "Akali"]

    def confirm_trip(self):
        print("Finding a driver...")
        while True:
            time.sleep(1)  
            driver = self.find_driver()
            if driver:
                print(f"The driver {driver} is accepting the trip..")
                return f"Trip confirmed with {driver}"
            else:
                print("The driver rejected the trip.")

    def find_driver(self):
        if random.choice([True, False]):
            return random.choice(self.available_drivers)
        else:
            return None

import random
import time
from ..auth.auth_manager import AuthManager

from ..models.trip import Trip

class TripManager:
    def __init__(self, auth_manager: AuthManager, trip: Trip):
        self.auth = auth_manager
        #self.pending_trips: list[Trip] = []
        self.trip = trip


    def confirm_trip(self, trip):
        self.trip = trip
        
        print(f"Finding a driver for your trip to {self.trip.dropoff}...")
        
        while True:
            time.sleep(1)  
            driver = self.find_driver()
            if driver.status:
                print(f"The driver {driver} is accepting the trip..")
                print(f"Trip confirmed with {driver}")
                self.trip.driver = driver
                return self.trip
            else:
                print("The driver rejected the trip.")

    def find_trip(self):
        print("🔄 Waiting for passengers...")
        try:
            while True:
                passenger = self.find_passenger()
                if passenger:
                    print(f"✅ Trip confirmed for {passenger.name} ({passenger.email})")
                    return passenger
                else:
                    print("⏳ No trips yet. Waiting...")
                    time.sleep(2)
        except KeyboardInterrupt:
            print("❌ Search cancelled by user.")
            return None

            
    def find_driver(self):
        return random.choice(self.auth.get_active_drivers())

    def find_passenger(self):
        if not self.auth.passengers:
            return None
        return random.choice(self.auth.passengers)

# trip1 = TripManager()
# print(trip1.find_trip())
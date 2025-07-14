import random
import time
from typing import Optional, List, Union
from ..auth.auth_manager import AuthManager
from ..models.trip import Trip
from ..auth.user import Driver

class TripManager:
    def __init__(self, auth_manager: AuthManager):
        self.auth = auth_manager
        self.pending_trips: list[Trip] = [Trip(dropoff="25 de Mayo 756", pickup="Av. de Mayo 1283", price=3500, driver=None, passenger=auth_manager.passengers[1], address_book=None),
                                          Trip(dropoff="Av. Calle Real 100", pickup="Blas Parera 452", price=6500, driver=None, passenger=auth_manager.passengers[0], address_book=None)]

    def confirm_trip(self, trip: Trip) -> Trip:
        print(f"Finding a driver for your trip to {trip.dropoff}...")
        self.pending_trips.append(trip)
        while trip.driver is None:
            time.sleep(1)
            print("⏳ Waiting for a driver...")
            trip.driver = self.auth.drivers[random.randint(0, len(self.auth.drivers)-1)]
        return trip

    def find_trip(self, driver: Driver) -> Trip | None:
        print("🔄 Waiting for trips...")
        try:
            if not self.pending_trips:
                print("⏳ No trips yet. Waiting...")
                time.sleep(2)
                return None
            
            trip = self.pending_trips.pop(0)
            trip.driver = driver
            print(f"✅ Trip accepted for {trip.passenger.name} to {trip.dropoff}")
            return trip
            
        except KeyboardInterrupt:
            print("❌ Search cancelled by user.")
            return None
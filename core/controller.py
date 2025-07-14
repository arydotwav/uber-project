from .trip_options import TripOptions
from .trip_manager import TripManager
from ..auth.auth_manager import AuthManager
from ..models.trip import Trip


class Controller:
    def __init__(self, auth_manager: AuthManager):
        self.trip_options = TripOptions()
        self.trip_manager = TripManager(auth_manager, trip= None)

    def get_addresses(self):
        return self.trip_options.get_addresses()

    def get_price_options(self):
        return self.trip_options.get_price_options()

    def confirm_trip(self, trip: Trip):
        return self.trip_manager.confirm_trip(trip)

    def find_trip(self):
        return self.trip_manager.find_trip()
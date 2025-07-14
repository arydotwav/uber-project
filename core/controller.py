from .trip_options import TripOptions
from .trip_manager import TripManager

class Controller:
    def __init__(self):
        self.trip_options = TripOptions()
        self.trip_manager = TripManager() 
        
    def get_addresses(self):
        return self.trip_options.get_addresses()

    def get_price_options(self):
        return self.trip_options.get_price_options()

    def confirm_trip(self):
        return self.trip_manager.confirm_trip() 
    
    def find_trip(self):
        return self.trip_manager.find_trip()
import time

from ..auth.user import Driver, Passenger
from .calification import Calification


class FollowUp:

    def __init__(self, driver: Driver):
        self.driver = driver
        self.calification_process : Calification = Calification()
        self.calification : int = None

    def show_info(self):
        print(f"Se ha confirmado el viaje con el conductor {self.driver.name}")
        time.sleep(1)
        print("Llegaras al destino en 5 minutos")
        time.sleep(2)
        print("You will arrive at your destination in 3 minutes")
        time.sleep(1)
        print("The trip has been completed successfully")
        time.sleep(1)
        self.calificate()
        return None
    
    def calificate(self):
        self.calification = self.calification_process.calificate()
        return self.calification
    

    
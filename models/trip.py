import random
from addresses_list import AddressList 
class TripUI:
    def __init__(self, pickup, dropoff, address_book):
        self.pickup = pickup
        self.dropoff = dropoff
        self.address_book = address_book

    def __str__(self):
        return f"pickup: {self.pickup} # droppoff: {self.dropoff}"

    def price(self):
        km = random.randint(1, 1000)
        #si le toca muchos km le va a salir más caro, suerte o suerte :P

        if km < 300:
            #el precio base del viaje es 20, se le suma el precio por km
            price = 20 + (km * 6.50)
            return f"price of trip: ${price}"
        elif km > 300:
            price = 20 + (km * 10.50)
            return f"price of trip: ${price}"
    
    def validate_addresses(self):
        print(self.address_book.check_address(self.pickup))
        print(self.address_book.check_address(self.dropoff))

# address_book = AddressList()
# trip1 = TripUI("emperanza 1061", "los pozos 1020", address_book)
# trip1.validate_addresses()

# print(trip1.price())
# print(trip1)
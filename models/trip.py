class Trip:
    def __init__(self, pickup, dropoff, address_book, passanger, driver, price):
        self.pickup = pickup
        self.dropoff = dropoff
        self.passanger = passanger
        self.driver = driver
        self.address_book = address_book
        self.price = price
    
    def validate_addresses(self):
        print(self.address_book.check_address(self.pickup))
        print(self.address_book.check_address(self.dropoff))

    def __str__(self):
        return f"Trip from {self.pickup} to {self.dropoff}, Passenger: {self.passenger.username}, Driver: {self.driver.username}, Price: ${self.price:.2f}"
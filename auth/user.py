from models.addresses_list import AddressList
class User:
    def __init__(self, name, telephone, email):
        self.name = name
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.telephone} | {self.email}"

class Passenger(User):
    def __init__(self, name, telephone, email, address_list=None):
        super().__init__(name, telephone, email)
        self.addresses = address_list if address_list else AddressList()

    def __str__(self):
        return f"{super().__str__()} | {self.addresses}"

class Driver(User):
    def __init__(self, name, telephone, email, status):
        super().__init__(name, telephone, email)
        self.status = status
    
    def return_status(self):
        if self.status is False:
            return f"Inactive"
        else:
            return f"Active"

    def __str__(self):
        return f"{super().__str__()} | {self.return_status()}"
    
# passenger1 = passenger("ariana", 1136608460, "arianarz268@gmail.com")
# driver1 = Driver("ariana", 1136608460, "arianarz268@gmail.com", False)
# print(driver1)
from models.addresses_list import AddressList
from typing import Optional
class User:
    def __init__(self, name: str, telephone: int, email: str) -> None:
        self.name: str = name
        self.telephone: int = telephone
        self.email: str = email

    def __str__(self) -> str:
        return f"{self.name} | {self.telephone} | {self.email}"

class Passenger(User):
    def __init__(self, name: str, telephone: int, email: str, address_list: Optional[AddressList] = None) -> None:
        super().__init__(name, telephone, email)
        self.addresses: AddressList = address_list if address_list else AddressList()

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.addresses}"

class Driver(User):
    def __init__(self, name: str, telephone: int, email: str, status: bool):
        super().__init__(name, telephone, email)
        self.status: bool = status
    
    def return_status(self) -> str:
        if self.status is False:
            return f"Inactive"
        else:
            return f"Active"

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.return_status()}"
    
# passenger1 = passenger("ariana", 1136608460, "arianarz268@gmail.com")
# driver1 = Driver("ariana", 1136608460, "arianarz268@gmail.com", False)
# print(driver1)
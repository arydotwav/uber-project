from models.addresses_list import AddressList
from .user import Passenger, Driver
from typing import Optional, List, Union
import re
class AuthManager:
    def __init__(self):
        self.passengers: list[Passenger] = [
            Passenger("alice", "1234", "alice@example.com"),
            Passenger("bob", "5678", "bob@example.com"),
        ]
        self.drivers = [
            Driver("draven", "5678", "draven@example.com", True),
            Driver("manaos", "12345", "manaos@example.com", True)
        ]
        self.logged_user = None

    def login(self, name: str, password: str) -> bool:
        for p in self.passengers:
            if p.name == name:
                if p.telephone == password:
                    self.logged_user = p
                    print(f"✅ Welcome {p.name} (passenger)!")
                    return True
                else:
                    print("❌ Incorrect password.")
                    return False
            
        for d in self.drivers:
            if d.name == name:
                if d.telephone == password:
                    d.status = True
                    self.logged_user = d
                    print(f"✅ Welcome {d.name} (driver)!")
                    return True
                else:
                    print("❌ Incorrect password.")
                    return False

        print("🆕 User not found. Let's register you.")
        while True:
            role = input("Are you a 'driver' or 'passenger'? ").strip().lower()
            if role in ["driver", "passenger"]:
                break
            else:
                print("Invalid role. Please enter 'driver' or 'passenger'.")
        

        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        while True:
            email = input("Enter your email: ")
            if re.match(email_regex, email):
                break
            else:
                print("Invalid email format. Please enter a valid email address.")

        if role == "passenger":
            address_list = AddressList()
            new_user = Passenger(name, password, email, address_list)
            self.passengers.append(new_user)
        elif role == "driver":
            new_user = Driver(name, password, email, False)
            self.drivers.append(new_user)

        self.logged_user = new_user
        print(f"✅ Registered and logged in as {role}: {new_user.name}")
        return True

    def logout(self) -> None:
        if self.logged_user:
            if isinstance(self.logged_user, Driver):
                self.logged_user.status = False
            print(f"👋 {self.logged_user.name} logged out.")
            self.logged_user = None
        else:
            print("⚠️ No user is currently logged in.")

    def get_current_user(self) -> Optional[Union[Driver, Passenger]]:
        # Logs
        print(f"Logged in as {self.logged_user.name}")
        print(self.logged_user)
        return self.logged_user

    def get_active_drivers(self) -> List[Driver]:
        return [driver for driver in self.drivers if driver.status]
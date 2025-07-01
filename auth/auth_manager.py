import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auth.user import Passanger, Driver
from models.addresses_list import AddressList  
class AuthManager:
    def __init__(self):
        self.passengers = [
            Passanger("alice", "1234", "alice@example.com"),
            Passanger("bob", "5678", "bob@example.com"),
        ]
        self.drivers = [
            Driver("draven", "5678", "draven@example.com", False),
            Driver("manaos", "12345", "manaos@example.com", True)
        ]
        self.logged_user = None

    def login(self, name, password):
        for p in self.passengers:
            if p.name == name and p.telephone == password:
                self.logged_user = p
                print(f"✅ Welcome {p.name} (passenger)!")
                return True
            
        for d in self.drivers:
            if d.name == name and d.telephone == password:
                d.status = True
                self.logged_user = d
                print(f"✅ Welcome {d.name} (driver)!")
                return True

        print("🆕 User not found. Let's register you.")
        role = input("Are you a 'driver' or 'passenger'? ").strip().lower()
        email = input("Enter your email: ")
        if role == "passenger":
            address_list = AddressList()
            new_user = Passanger(name, password, email, address_list)
            self.passengers.append(new_user)
        else:
            new_user = Driver(name, password, email, False)
            self.drivers.append(new_user)

        self.logged_user = new_user
        print(f"✅ Registered and logged in as {role}: {new_user.name}")
        return True

    def logout(self):
        if self.logged_user:
            if isinstance(self.logged_user, Driver):
                self.logged_user.status = False
            print(f"👋 {self.logged_user.name} logged out.")
            self.logged_user = None
        else:
            print("⚠️ No user is currently logged in.")

    def get_current_user(self):
        return self.logged_user

    def get_active_drivers(self):
        return [driver for driver in self.drivers if driver.status]
import time
import random

from ..core.trip_manager import TripManager
from .follow_up import FollowUp
from ..auth.user import Driver, Passenger
from ..core.controller import Controller
from ..auth.auth_manager import AuthManager
from ..models.trip import Trip


class TripUi(Controller):
    def __init__(self, auth_manager: AuthManager):
        super().__init__(auth_manager)
        self.auth = auth_manager
        self.follow: FollowUp = None
        self.trips_history = []  
        
    def welcome(self):
        print("----  Uber  ----")
        time.sleep(1)
        print("Welcome! Please log in!")

    def login(self):
        while True:
            username = input("Username: ")
            password = input("Phone (used as password): ")

            if self.auth.login(username, password):
                self.user = self.auth.get_current_user()
                print(f"✅ Welcome, {self.user.name}!")
                break
            else:
                print("❌ Login failed. Please try again.")

    def _driver_flow(self):
        while True:
            show_as_active = input("(Driver) Do you want to show as active? (y/n): ").lower()
            if show_as_active == 'y':
                self.user.status = True
                trip = self.find_trip(self.user)
                if trip:
                    print(f"You have a trip with passenger: {trip.passenger.name} ({trip.passenger.email})")
                    print(f"Pickup: {trip.pickup}")
                    print(f"Dropoff: {trip.dropoff}")
                    print("You are 5 minutes from your destination")
                    time.sleep(1)
                    print("You are 2 minutes from your destination")
                    time.sleep(1)
                    print("You are at your destination")
                    input("Press Enter to complete the trip...")
                    print("Trip completed.")
                else:
                    print("No passenger found at this time.")
            else:
                print("You will remain inactive.")
                break

    def _passenger_flow(self):
        print("Your addresses:")
        addresses = self.get_addresses()
        for i, address in enumerate(addresses):
            print(f"{i+1}. {address}")
        print(f"{len(addresses) + 1}. Enter a new address")

        while True:
            try:
                address_choice = int(input("Choose a pickup address: "))
                if 1 <= address_choice <= len(addresses) + 1:
                    break
                else:
                    print("❌ Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        
        if address_choice == len(addresses) + 1:
            new_address = input("Enter the new address: ")
            self.trip_options.address_list.check_address(new_address)
            pickup_address = new_address
        else:
            pickup_address = addresses[address_choice - 1]

        while True:
            try:
                address_choice = int(input("Choose a dropoff address: "))
                if 1 <= address_choice <= len(addresses) + 1:
                    if address_choice == len(addresses) + 1:
                        new_address = input("Enter the new address: ")
                        dropoff_address = new_address
                    else:
                        dropoff_address = addresses[address_choice - 1]

                    if dropoff_address == pickup_address:
                        print("❌ Dropoff address cannot be the same as pickup address. Please choose a different one.")
                    else:
                        self.trip_options.address_list.check_address(dropoff_address)
                        break
                else:
                    print("❌ Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        print("Price options:")
        prices = self.get_price_options()
        for i, (option, price) in enumerate(prices.items()):
            print(f"{i+1}. {option}: ${price}")

        try:
            price_choice = int(input("Choose a price option: "))
            if price_choice < 1 or price_choice > len(prices):
                print("Invalid option selected.")
                return

            selected_price = list(prices.values())[price_choice - 1]
            print(f"Selected price: ${selected_price}")

            trip = Trip(
                pickup=pickup_address,
                dropoff=dropoff_address,
                address_book=self.trip_options.address_list,
                passenger=self.user,
                driver=None,
                price=selected_price
            )
            confirmed_trip = self.confirm_trip(trip)

            if confirmed_trip:
                self.follow = FollowUp(driver=confirmed_trip.driver)
                self.follow.show_info()
                self.trips_history.append({
                    "pickup": confirmed_trip.pickup,
                    "dropoff": confirmed_trip.dropoff,
                    "price": confirmed_trip.price
                })
        except ValueError:
            print("Please enter a valid number.")

    def show_trips_history(self):
        print("-- new section starts --")
        print("trips history:")
        total_spent = 0
        for trip in self.trips_history:
            print(f"Trip from {trip['pickup']} to {trip['dropoff']} with price {trip['price']}")
            total_spent += trip['price'] 
        print(f"Total trips: {len(self.trips_history)}")
        print("-- new section ends --")
        print(f"Total spen: ${total_spent}")

    def start_trip(self):
        self.welcome()
        self.login()

        while True:
            if isinstance(self.user, Passenger):
                self._passenger_flow()
            elif isinstance(self.user, Driver):
                self._driver_flow()

            logout_option = input("Do you want to logout? (y/n): ").lower()
            if logout_option == 'y':
                self.auth.logout()
                print("Closing the app.")
                self.show_trips_history()
                break
            else: 
                print("You will stay logged in.")
                another_session = input("Do you want to search for a new trip? (y/n): ").lower()
                if another_session != 'y':
                    print("Closing the app.")
                    self.show_trips_history()
                    break

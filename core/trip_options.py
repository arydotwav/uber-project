import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.addresses_list import AddressList

class TripOptions:
    def __init__(self):
        self.address_list: AddressList = AddressList()

    def get_addresses(self):
        addresses = self.address_list.get_all_addresses()
        if addresses:
            return addresses()
        else:
            return "message_no_addreses"

    def get_price_options(self):
        return {
            "Economy": 3500,
            "Fast": 6500,
            "Confort": 12000
        }
 
# trip1 = TripOptions()
# print(trip1.get_addresses())
from models.addresses_list import AddressesList

class TripOptions:
    def __init__(self):
        self.address_list = AddressesList()

    def get_addresses(self):
        addresses = self.address_list.get_all_addresses()
        if addresses:
            return addresses
        else:
            return "message_no_addreses"

    def get_price_options(self):
        return {
            "Ecomy": 3500,
            "Fast": 6500,
            "Confort": 12000
        }
 
 
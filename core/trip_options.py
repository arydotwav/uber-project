from ..models.addresses_list import AddressList
from typing import Optional, List, Union, Dict

class TripOptions:
    def __init__(self) -> None:
        self.address_list: AddressList = AddressList()

    def get_addresses(self) -> Union[list, str]:    
        addresses = self.address_list.get_all_addresses()
        if addresses:
            return addresses
        else:
            return "message_no_addreses"

    def get_price_options(self) -> Dict[str, int]:
        return {
            "Economy": 3500,
            "Fast": 6500,
            "Confort": 12000
        }
 
# trip1 = TripOptions()
# print(trip1.get_addresses())
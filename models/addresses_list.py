class AddressList:
    def __init__(self):
        self.list = [
            "avenida 1061",
            "hola que tal 1010"
        ]

    def check_address(self, address):
        if address in self.list:
            return address
        else:
            print(f"{address} not in saved list.")
            option = int(input("would you like to add this address to your saved list?\n1 - YES\n2 - NO\nOption: "))
            if option == 1:
                self.list.append(address)
                return f"address {address} saved. selected for trip."
            else:
                return(f"{address} not saved. still selected for trip")
           
    def get_all_addresses(self):
        return self.list
        
    def __str__(self):
        return f"YOUR ADDRESSES: {', '.join(self.list)}"
        
    
# address = AddressList()
# print(address.check_address("emperanza 1061"))
# print(address)
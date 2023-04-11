import pprint


class Address:

    def __init__(self, street_num, street_name, postcode, state, country):
        self.street_num = street_num
        self.street_name = street_name
        self.postcode = postcode
        self.state = state
        self.country = country

    def postage_address(self):
        return f"{self.street_num}, {self.street_name}, {self.postcode}, {self.state}, {self.country}"

    def __repr__(self):
        return f"Address('{self.street_num}', '{self.street_name}', {self.postcode}, {self.state})"

    def __str__(self):
        return f"{self.postage_address()}"


class AddressBook:

    def __init__(self, addresses=None):
        if addresses == None:
            self.addresses = []
        else:
            self.addresses = addresses

    def add_address(self, address):
        if len(self.addresses) <= 4:
            if address not in self.addresses:
                self.addresses.append(address)
                print(f"Address '{address}' added to address book")
            else:
                print(f"Address: '{address}', already exists in address book")

        else:
            raise Exception("Amount of addresses exceeded. Maximum of 5 addresses per address book")

    def print_address(self, index):
        print("Address:", self.addresses[index])
    
    def remove_address(self, index):
        if self.addresses is not None:
            del self.addresses[index]
            print(f"Address '{self.addresses[index]}' removed from address book")
        else:
            print("Address book is empty")
    
    def clear_all(self):
        self.addresses.clear()

    def search(self, field, value):
        matches = []

        field = field.lower()
        value = value.lower()

        for address in self.addresses:
            if address.__dict__[field].lower() == value.lower():
                matches.append(address)

        return matches
                
    def __repr__(self):
        return f"AddressBook('{self.addresses}')"


add_1 = Address("10", "Test St", "90210", "California", "America")
add_2 = Address("11", "Test Rd", "90211", "California", "America")
add_3 = Address("12", "Test Dr", "90212", "California", "America")
add_4 = Address("13", "Test Ave", "90213", "California", "America")
add_5 = Address("14", "Test Ln", "90214", "Mexico", "America")
add_6 = Address("15", "Test Blvd", "90215", "California", "America")

add_book = AddressBook()
# add_book.add_address(add_1)
# add_book.add_address(add_2)
# add_book.add_address(add_3)
# add_book.add_address(add_4)
# add_book.add_address(add_5)

# add_book.search("state", "California")

# add_book.search("California")

# add_book.add_address(add_6)

# add_book.print_address(1)

# pprint.pprint(add_book.addresses)
# print(repr(add_book))

# add_book.clear_all()

# print(add_book)

# add_book.remove_address(1)
# pprint.pprint(add_book.addresses)

# add_1 = Address("10", "Test rd", "90210", "California", "America")
# print(add_1.postage_address())
# print(repr(add_1))
# print(str(add_1))

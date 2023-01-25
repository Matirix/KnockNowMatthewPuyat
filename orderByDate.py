# Name : Matthew Puyat


class Listings:
    """
    This class is used to create a Listing.
    """
    def __init__(self, name: str, address: str, date: int):
        """
        This is the Initializer for the Listings class.
        :param name: a string
        :param address: an address
        :param date: a date
        """
        self._name = name
        self._address = address
        self._date = date

    def get_date(self):
        """
        This method returns the date of the listing.
        :return: an int
        """
        return self._date

    def get_address(self):
        """
        This method returns the address of the listing.
        :return: a string
        """
        return self._address

    def get_name(self):
        """
        This method returns the name of the listing.
        :return: a string
        """
        return self._name

    def __repr__(self):
        """
        This method returns the name, address, and date of the listing.
        :return: a string
        """
        return f"{self._name} {self._address} {self._date}"


class ListingsList:
    """
    This class is used to create a manage Listings.
    """
    def __init__(self):
        """
        This is the Initializer for the ListingsList class.
        """
        self._listings = list()

    def add_listing(self, listing: Listings):
        """
        This method adds a listing to the list of listings.
        :param listing: a Listing
        """
        self._listings.append(listing)

    def sort_list_by_date(self) -> list:
        """
        This method sorts the list of listings by date.
        :return: a Sorted List
        """
        return sorted(self._listings, key=lambda listing: listing.get_date(), reverse=True)

    def remove_duplicates(self) -> list:
        """
        This method removes duplicate listings
        :precondition: the list must be sorted by date.
        :return: a no-duplicate list
        """
        # First Address
        first_address = self.sort_list_by_date()[0].get_address()
        # Make a copy of the sorted list
        updated_lists = self.sort_list_by_date()

        # Skips the first recent address and compares it with everything else, if it is a duplicate, it removes it.
        # Since the list is already sorted by date, the first recent address will always be the first address in
        # the list.
        for i in range(1, len(updated_lists)):
            if self.is_duplicate(first_address, self.sort_list_by_date()[i].get_address()):
                updated_lists.remove(self.sort_list_by_date()[i])
        return updated_lists

    @staticmethod
    def is_duplicate(first_address, second_address) -> bool:
        """
        This method checks if the two addresses are the same.
        :param first_address: a string
        :param second_address: a string
        :return: true if first address is the same as second address
        """
        return first_address == second_address

    def get_most_recent_listings(self) -> tuple:
        """
        This method returns the most recent listings using the indexes of the sorted list.
        :return: a tuple
        """
        return tuple([self.remove_duplicates()[0].get_name(), self.remove_duplicates()[1].get_name()])

    def print_sorted_listings(self):
        """
        This method prints the sorted list of listings.
        """
        for i in self.sort_list_by_date():
            print(i.get_name(), i.get_address(), i.get_date())


def insert_data(listings):
    """
    This function inserts data into the listings list.
    """
    listings.add_listing(Listings("L4", "123 kings road", 2022))
    listings.add_listing(Listings("L1", "123 kings road", 2020))
    listings.add_listing(Listings("L2", "20 queen road", 1990))
    listings.add_listing(Listings("L3", "21 queen road", 1996))
    listings.add_listing(Listings("L4", "22 queen road", 1993))
    listings.add_listing(Listings("L5", "23 queen road", 1994))
    listings.add_listing(Listings("L6", "24 queen road", 1993))
    listings.add_listing(Listings("L4", "123 kings road", 2012))
    return listings


def main():
    # Create a new ListingsList
    listings = ListingsList()
    # Insert data into the ListingsList
    insert_data(listings)
    # Print the sorted list of listings
    print(listings.get_most_recent_listings())


if __name__ == "__main__":
    main()

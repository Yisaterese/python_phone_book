import pytest

from phone_book import PhoneBook



def test_if_phone_book_can_add_contacts():
    phone_book = PhoneBook()
    phone_book.add_contacts("Ada", "07890876543")
    assert phone_book.list_of_contacts() == 1


def test_contact_can_be_deleted():

    phone_book = PhoneBook()
    phone_book. add_contacts("Ada", "07890876543")
    phone_book.add_contacts("john", "07890876543")
    phone_book.delete_contact("Ada")
    assert phone_book.list_of_contacts() == 1

def test_can_search_for_contacts():
    phone_book = PhoneBook()
    phone_book.add_contacts("Ada", "07890876543")
    phone_book.add_contacts("john", "07890876543")
    phone_book.delete_contact("Ada")
    assert phone_book.list_of_contacts() == 1
    assert phone_book.search_contact("john") == "contact name exists in phone book"





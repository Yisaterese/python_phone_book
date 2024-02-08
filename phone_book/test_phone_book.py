import pytest

from phone_book import PhoneBook



def test_if_phone_book_can_add_contacts():
    phone_book = PhoneBook()
    assert phone_book.length_of_contact_list() == 0
    phone_book.add_contacts("Ada", "07890876543")
    assert phone_book.length_of_contact_list() == 1


def test_phone_book_is_empty_before_adding_contact():
    phone_book2 = PhoneBook()
    assert phone_book2.length_of_contact_list() == 0


def test_contact_can_be_deleted():

    phone_book1 = PhoneBook()
    assert phone_book1.length_of_contact_list() == 0
    phone_book1. add_contacts("Ada", "07890876543")
    phone_book1.add_contacts("john", "07890876543")
    assert phone_book1.length_of_contact_list() == 2

    phone_book1.delete_contact("Ada")
    assert phone_book1.length_of_contact_list() == 1

    phone_book1.clear_contact_list()
    assert phone_book1.length_of_contact_list() == 0


def test_can_search_for_contacts():
    phone_book = PhoneBook()
    phone_book.add_contacts("Ada", "07890876543")
    phone_book.add_contacts("john", "07890876543")
    assert phone_book.search_contact("john") == True
    assert phone_book.length_of_contact_list() == 2

    phone_book.clear_contact_list()
    assert phone_book.length_of_contact_list() == 0


def test_can_clear_all_contact_list():
    phone_book = PhoneBook()

    assert phone_book.length_of_contact_list() == 0
    phone_book.add_contacts("Ada", "07890876543")
    phone_book.add_contacts("john", "07890876543")

    phone_book.clear_contact_list()
    assert phone_book.length_of_contact_list() == 0




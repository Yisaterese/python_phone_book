
from phone_book import PhoneBook

def test_if_phone_book_can_add_contacts():
    book = PhoneBook()
    assert book.add_contacts("Ada","07890876543") == 1
    assert book.add_contacts("Ada","07890876543") == 2
    assert book.add_contacts("john", "07890876543") == 3

def test_display_contact_list():
    book = PhoneBook()
    assert book.add_contacts("Ada", "07890876543") == 1
    assert book.add_contacts("Ada", "07890876543") == 2
    assert book.add_contacts("john", "07890876543") == 3

    assert book.delete_contact("Ada") == 2
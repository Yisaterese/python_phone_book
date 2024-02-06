
from phone_book import *

def test_save_contacts():
    book = phone_book()
    book.add_contacts("Ada","57890876543")
    added_contact = book.search_contact("Ada")
    assert  added_contact == "Ada"




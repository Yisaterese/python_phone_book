
import pytest
from phone_book import *

#@pytest.fixture

def test_save_contacts():
    phone_book.save_contacts(524238162353,"ada",)
    assert "ada",524238162353 in  phone_book.save_contacts( phone_book)




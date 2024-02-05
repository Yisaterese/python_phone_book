class phone_book:
    def __init__(self,contacts = []):
        self.contacts = contacts

    def save_contacts(self,phone_number,name):
        phone_book = {}
        phone_book[name] = phone_number
        self.append(phone_book)

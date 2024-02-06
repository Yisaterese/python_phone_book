class phone_book:
    def __init__(self,contacts_list = []):
        self.contacts_list = contacts_list

    def save_contacts(self,name,phone_number):
        for index in range(len(name)):
            if index != 11:
                return "Enter a valid number with eleven digits"
        contact = {"name":name,"phone_umber":phone_number}
        self.contacts_list.append(contact)

    def serch_contact(self,name):
        for contact in self.contacts_list:
           if contact["name"] == name:
               return contact

    def delete_contact(self,delete_contact):
        for contact in self.contacts_list:
            if contact["name"] == delete_contact:
                self.contacts_list.pop(delete_contact)





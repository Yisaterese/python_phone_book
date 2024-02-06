import sys


class PhoneBook:
    def __init__(self, contacts_list=[]):
        self.contacts_list = contacts_list


    def add_contacts(self, name, phone_number):
        if len(phone_number) == 11 and phone_number.startswith("0"):
            contact = {"name": name, "phone_number": phone_number}
            self.contacts_list.append(contact)
        return len(self.contacts_list)

    def delete_contact(self, delete_contact):
        for contact in self.contacts_list:
            if contact["name"] == delete_contact:
                self.contacts_list.remove(contact)


'''  def search_contact(self, name):
        for contact in self.contacts_list:
            if contact["name"] == name:
                return contact.get(name)
            else:
                return "contact not found"

    def display_contact(self, contacts_list):
        contact_lst = []
        for numbers in range(len(contacts_list)):
            if numbers in contacts_list:
                contact_lst.append(numbers)
                return contact_lst
            else:
                return "contact not found"

   

    def exit(self, sentinel):

        def contact_menu(self, option):
            sys.exit()

            while True:
                print("""1. Add contact
                         2. Delete contact
                         3. Search contact
                         4. Exit
                           """)
                option = input(int("select option between 1 and 4: "))
                if option == 1:
                    self.add_contact()
                    self.contact_menu()
                elif option == 2:
                    self.dellete_contact()
                    self.contact_menu()
                elif option == 3:
                    self.serch_contact()
                    self.contact_menu()
                elif option == 4:
                    break
                    exit()
                    print("Goodbye thanks for banking with us")
            else:
                print("select a valid option")'''

class PhoneBook:



    def __init__(self, contacts_list=[]):
        self.contacts_list = contacts_list
        #self.list_of_contacts = len(self.contacts_list)

    def add_contacts(self, name, phone_number):
        if len(phone_number) == 11 and phone_number.startswith("0"):
            contact = {"name": name, "1phone_number": phone_number}
            self.contacts_list.append(contact)

    def length_of_contact_list(self):
        if not self.contacts_list:
            return 0
        else:
            return len(self.contacts_list)

    def delete_contact(self, delete_name):
        for the_contacts in self.contacts_list:
            if the_contacts["name"] == delete_name:
                self.contacts_list.remove(the_contacts)
                break


    def search_contact(self, name):
        for my_contacts in self.contacts_list:
            if my_contacts["name"] == name:
                return True

        return False


    def clear_contact_list(self):
        if self.contacts_list:
            self.contacts_list.clear()

    #
    # def display_contact(self, contacts_list):
    #     contact_lst = []
    #     for numbers in range(len(contacts_list)):
    #         if numbers in contacts_list:
    #             contact_lst.append(numbers)
    #             return contact_lst
    #         else:
    #             return "contact not found"
    #
    #
    #
    # def exit(self, sentinel):
    #
    #     def contact_menu(self, option):
    #         sys.exit()
    #
    #         while True:
    #             print("""1. Add contact
    #                      2. Delete contact
    #                      3. Search contact
    #                      4. Exit
    #                        """)
    #             option = input(int("select option between 1 and 4: "))
    #             if option == 1:
    #                 self.add_contact()
    #                 self.contact_menu()
    #             elif option == 2:
    #                 self.dellete_contact()
    #                 self.contact_menu()
    #             elif option == 3:
    #                 self.serch_contact()
    #                 self.contact_menu()
    #             elif option == 4:
    #                 break
    #                 exit()
    #                 print("Goodbye thanks for banking with us")
    #         else:
    #             print("select a valid option")

class my_phone:
    def __int__(self):
        self.contacts = {}

    def delete_contact(self, name_to_delete):
        if name_to_delete in self.contacts:
            del self.contacts[name_to_delete]

    def display_contact(self):
        return list(self.contacts.keys())

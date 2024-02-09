import cmd

class AddressBook(cmd.Cmd):
    intro = "Welcome to my Address Book . Type 'help' for commands.\n"
    prompt = "(Address Book)>"


    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """ Adds a new contact to the address book. Usage: add <phone> <name>"""
        phone, name = args.split()
        if phone not in self.contacts:
            self.contacts[phone] = name
            print(f"Contacts addeded succesfully {phone} - {name}")
        else:
            print(f"Contacts {Phone} alreadly exists. Use 'update' to update contacts")

    def do_read(self,args):
        """Reads all contacts """
        if not self.contacts:
            print("No contacts found")
        else:
            for phone, name in self.contacts.items():
                print(f" {phone} - {name}")
    def do_update(self, args):
        """updates a contact .usage: <phone> <new_name> """
        phone, new_name = args.split()
        if phone in self.contacts:
            self.contacts[phone] = new_name
            print(f"Contacts name updated: {phone} - {new_name}.")
        else:
            print(f"{number} not found. use add to create contacts")

    def do_delete(self, args):
        """Deletes a contact. Usage :delete <phone> """
        phone = args
        if phone in self.contacts:
            del self.contacts[phone]
            print(f"Deleted contact : {phone}")

        else:
            print(f"Contacts not found")

    def do_exist(self, args):
        """Exits our address book """
        return True


if __name__ == "__main__":
    AddressBook().cmdloop()


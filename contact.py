class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class Contact_Book:
    def __init__(self):
        self.contacts = []
    def addcontact(self, contact):
        self.contacts.append(contact)
    def viewcontacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print("-" * 20)
    def searchcontact(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.name or query in contact.phone:
                results.append(contact)
        return results
    def updatecontact(self, name, updated_info):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = updated_info.get("phone", contact.phone)
                contact.email = updated_info.get("email", contact.email)
                contact.address = updated_info.get("address", contact.address)
                break
    def deletecontact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
if __name__ == '__main__':
    contactbook = Contact_Book()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contactbook.addcontact(contact)
        elif choice == 2:
            contactbook.viewcontacts()
        elif choice == 3:
            query = input("Enter name or phone to search: ")
            results = contactbook.searchcontact(query)
            if results:
                for contact in results:
                    print(f"Name: {contact.name}")
                    print(f"Phone: {contact.phone}")
                    print("-" * 20)
            else:
                print("No contacts found.")
        elif choice == 4:
            name = input("Enter name of contact to update: ")
            updated_info = {}
            if input("Update phone?: ").lower() == "y":
                updated_info["phone"] = input("Enter new phone: ")
            if input("Update email? : ").lower() == "y":
                updated_info["email"] = input("Enter new email: ")
            if input("Update address?:").lower() == "y":
                updated_info["address"] = input("Enter new address: ")
            contactbook.updatecontact(name, updated_info)
        elif choice == 5:
            name = input("Enter name of contact to delete: ")
            contactbook.deletecontact(name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

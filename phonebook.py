import time
def main_menu():
    print("PHONEBOOK")
    print("================================")
    print("What would you like to do? (❁´◡`❁)📖")
    print("1. Show all contact\n2. Add new contact\n3. Delete contact\n4. Search contact\n5. Update contact\n6. Exit ")
    print("================================")


main_menu()
phonebook = int(input("Reply: "))

def displayContact():
    if len(contact) == 0:
        print("You contact is empty")
        print()
    else:
        print("=======================================")
        time.sleep(3)
        print(f"{'name'} {'Number':>20}")
        for key, value in contact.items():
            time.sleep(3)
            print(f"{key} {value:>20}")
        print("=======================================")


def delete_contact():
    number_to_delete = input(" Enter the name to delete: ")
    if number_to_delete in contact:
        contact.pop(number_to_delete)
        time.sleep(2)
        print("Delete successful")
    else:
        print(f"{number_to_delete} does not exist")


def search_contact():
    number_to_search = input("Enter the name you want to search: ")
    print("Searching..."
          "")
    if number_to_search in contact:
        time.sleep(3)
        print(f"{number_to_search} {contact[number_to_search]}")
    else:
        time.sleep(2)
        print(f"{number_to_search} does not exist")


"""def update_contact():
    reply = int(input("Enter 1 to change name or 2 to change number: "))

    if (reply == 1):
        old_name = input("Enter old_name: ")
        new_name = input("Enter new_name: ")
        if old_name in contact:
            contact[old_name] = new_name
            contact.update({old_name : new_name})
            print("Change successful")

        else:
            print(f"{old_name} does not exist")

    elif reply == 2:
        old_number = input("Enter old_number: ")
        new_number = input("Enter new_number: ")
        if old_number in contact:
            contact.update({old_number: new_number})
            print("Changed successful")
        else:
            print(f"{old_number} does not exist")
"""
def update_contact():
    reply = int(input("Enter 1 to change name or 2 to change number: "))
    if reply == 1:
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")
        if old_name in contact:
            contact[new_name] = contact.pop(old_name)
            print("Change successful 😂😂😂😂😂")
        else:
            print(f"{old_name} does not exist 😒😒😒😒😒")

    elif reply == 2:
        name = input("Enter name: ")
        if name in contact:
            new_number = input("Enter new number:😂😂😂😂😂 ")
            contact[name] = new_number
            print("Changed successful")
        else:
            print(f"{name} does not exist")

contact = {}

while True:
    if phonebook == 1:
        displayContact()
    elif phonebook == 2:
        number = input("Enter number: ")
        name = input("Enter name: ")
        contact[name] = number
    elif phonebook == 3:
        delete_contact()
    elif phonebook == 4:
        search_contact()
    elif phonebook == 5:
        update_contact()
    elif phonebook == 6:
        print("NOTE:")
        time.sleep(5)
        print(
                "This is the first prototype of this application. The programme is still a work in progress. Give us your a feedback by dropping a comment. ");
        print("Made by Jumong")
        time.sleep(5)
        print("Goodbye and Thank You!!!")
        break
    else:
        print("Number should be between 1 - 6")

    main_menu()
    phonebook = int(input("Reply: "))

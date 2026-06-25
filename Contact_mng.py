# Creating a program that lets a user manage a list of contacts through a menu
# Add, searc, view, and delete contacts by name
# Jonathan Dotse, 06/22/26

# Initializing dictionary to hold contacts
contact_list = {}

# Initializing while loop

while True:
    print("Contact Manager")
    print("----------------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    user_input = int(input("Enter your choice: "))

    # Initializing if statements

    if user_input == 1:
        name = str(input("Enter name: "))
        phone_number = str(input("Enter phone number: "))

        contact_list[name] = phone_number

        print("Contact added successfully.")

    elif user_input == 2:
        name = str(input("Enter name to search the contact"))
        if name in contact_list:
            print(name + ": " + contact_list[name])

        else:
            print("Contact not found.")
    
    elif user_input == 3:
        pass

    elif user_input == 4:
        pass

    elif user_input == 5:
        break

    else:
        print("Input not valid")
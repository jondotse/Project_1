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
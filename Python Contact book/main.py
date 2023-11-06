contacts_append = open("contacts.txt", "a")  # To add contacts
contacts_view = open("contacts.txt", "r")  # To view contacts


# What will be displayed when user runs program
def starting_screen():
    start_screen = """
     _____________________________________________________________________________
    |                                                                             |
    | Welcome to contact book in python!, Press any key and hit enter to start... |
    |_____________________________________________________________________________|
    
    """
    print(start_screen)


start = input(">> ")


# Main event handling such as the mode the user wants
def contact_book():
    mode = input("Would you like to view (v), or add (a), A contact? ")

    if mode == "v":  # For viewing
        print(contacts_view.read())
    elif mode == "a":  # For writing
        contact_name = input("Please enter the name of your contact: \n")
        contact_number = input("Please enter the phone number of your contact: \n")

        contacts_append.write(contact_name + ": " + contact_number)  # Writing contacts to file


contact_book()

# To see if user wants to make the program run again
again = input("Would you like to start program again (y/n)? ")

while True:
    if again == "y":
        contact_book()
    elif again == "n":
        print("Okay! Done.")
        break

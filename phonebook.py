import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)  
    except json.JSONDecodeError:
        print("Error: Invalid JSON in contacts.json")
        exit(1) 


def save_contacts(data):
    try:
        with open("contacts.json", "w") as file:
            json.dump(data, file, indent=2)  
    except Exception as e:
        print(f"Error saving contacts: {e}")
        exit(1)


def add_contact():
    name = input("Enter the name of the new contact: ")
    number = input("Enter the phone number: ")
    new_contact = {
        "name": name,
        "number": number,
        "metadata": {
            "added_by": "user", 
            "source": "manual entry",  
            "tags": []  
        }
    }
    contacts = load_contacts()
    contacts.append(new_contact)

    save_contacts(contacts)
    print("Saved!")


def display_contacts():
    contacts = load_contacts()
    print("\nCurrent contacts:")
    print(json.dumps(contacts, indent=2))  

print("Welcome to your JSON-powered phonebook")
add_contact()  
display_contacts() 
def main():
    while True:
        print("\nMenu:")
        choice = input("1. Add a new contact \n 2. Quit \n Choose an option (1/2/): ")
        if choice == "1":
            add_contact()  
        elif choice == "2":
            print("Goodbye!")
            break 
        else:
            print("Invalid choice. Please choose a valid option.")
        display_contacts() 

if __name__ == "__main__":
    main()

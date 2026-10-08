import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)

        if isinstance(contacts, list):
            return contacts

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def list_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")


def search_contacts(contacts):
    """Search contacts by part of their name."""
    search_name = input("Enter name to search: ").strip().lower()

    matches = [
        contact for contact in contacts
        if search_name in contact["name"].lower()
    ]

    if not matches:
        print("No matching contacts found.")
        return

    print("\n--- Search Results ---")

    for contact in matches:
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def edit_contact(contacts):
    """Edit an existing contact."""
    if not contacts:
        print("No contacts available.")
        return

    list_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to edit: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        contact = contacts[number - 1]

        print("\nPress Enter to keep the existing value.")

        name = input(f"Name [{contact['name']}]: ").strip()
        phone = input(f"Phone [{contact['phone']}]: ").strip()
        email = input(f"Email [{contact['email']}]: ").strip()

        if name:
            contact["name"] = name

        if phone:
            contact["phone"] = phone

        if email:
            contact["email"] = email

        save_contacts(contacts)

        print("Contact updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_contact(contacts):
    """Delete a contact."""
    if not contacts:
        print("No contacts available.")
        return

    list_contacts(contacts)

    try:
        number = int(input("\nEnter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted_contact = contacts.pop(number - 1)
        save_contacts(contacts)

        print(f"Contact '{deleted_contact['name']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Display the main menu."""
    print("\n==============================")
    print("       CONTACT BOOK")
    print("==============================")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contacts")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")
    print("==============================")


def main():
    contacts = load_contacts()

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            list_contacts(contacts)

        elif choice == "3":
            search_contacts(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
# Contact Book

A simple menu-driven contact book built with Python.

## Features

* Add contacts
* List all contacts
* Search contacts by part of a name
* Edit existing contacts
* Delete contacts
* Store contacts in a JSON file
* Contacts remain saved after restarting the program
* Automatically starts with an empty contact list if the JSON file is missing or broken

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python contact_book.py
```

If `python` does not work on Windows, try:

```bash
py contact_book.py
```

## How It Works

The program stores contacts in a file called `contacts.json`.

Each contact contains:

* Name
* Phone number
* Email address

The JSON file is created automatically when the first contact is added.

If the JSON file is missing or contains invalid data, the program starts with an empty contact list.

## Example Menu

```text
==============================
       CONTACT BOOK
==============================
1. Add contact
2. List contacts
3. Search contacts
4. Edit contact
5. Delete contact
6. Exit
==============================
```

## Project Structure

```text
contact-book/
│
├── contact_book.py
├── README.md
└── contacts.json   # created automatically
```

## Author

Harshit Pal

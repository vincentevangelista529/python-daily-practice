import json

def get_non_empty_input(prompt):
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty.")
        value = input(prompt).strip()
    return value


def get_valid_age():
    while True:
        age = input("Enter age: ")

        if not age.isdigit():
            print("Age must be a number.")
            continue

        age = int(age)

        if age < 1 or age > 120:
            print("Age must be between 1 and 120.")
            continue

        return age


def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


def add_user():
    profile = {}
    profile["name"] = get_non_empty_input("Enter name: ")
    profile["age"] = get_valid_age()
    users.append(profile)
    save_users()
    print("User added and saved!")


def show_users():
    if not users:
        print("No users yet.")
        return

    print("\n--- Users ---")
    for index, user in enumerate(users, start=1):
        print(f"{index}. Name: {user['name']}, Age: {user['age']}")


while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

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

def search_users():
    if not users:
        print("No users to search.")
        return

    keyword = input("Enter name to search: ").strip().lower()

    if not keyword:
        print("Search cannot be empty.")
        return

    found = False

    print("\n--- Search Results ---")
    for index, user in enumerate(users, start=1):
        if keyword in user["name"].lower():
            print(f"{index}. Name: {user['name']}, Age: {user['age']}")
            found = True

    if not found:
        print("No matching users found.")

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


def add_user():
    profile = {}
    profile["name"] = get_non_empty_input("Enter name: ")
    profile["age"] = get_valid_age()
    users.append(profile)
    save_users(users)
    print("User added and saved!")


def show_users():
    if not users:
        print("No users yet.")
        return

    print("\n--- Users ---")
    for index, user in enumerate(users, start=1):
        print(f"{index}. Name: {user['name']}, Age: {user['age']}")

def select_user_index(action):
    if not users:
        print(f"No users to {action}.")
        return None

    show_users()
    choice = input(f"Enter user number to {action}: ")

    if not choice.isdigit():
        print("Invalid input.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(users):
        print("User number out of range.")
        return None

    return index

def edit_user():
    index = select_user_index("edit")
    if index is None:
        return

    user = users[index]

    new_name = input(f"New name ({user['name']}): ").strip()
    if new_name:
        user["name"] = new_name

    new_age = input(f"New age ({user['age']}): ").strip()
    if new_age.isdigit():
        age = int(new_age)
        if 1 <= age <= 120:
            user["age"] = age

    save_users(users)
    print("User updated successfully.")
  
def delete_user():
    index = select_user_index("delete")
    if index is None:
        return

    deleted_user = users.pop(index)
    save_users(users)

    print(f"Deleted user: {deleted_user['name']}")


while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Edit User")
    print("4. Delete User")
    print("5. Search User")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        edit_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        search_users()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

users = []

def add_user():
  profile = {}
  profile ["name"] = input("Enter name: ")
  profile ["age"] = input("Enter age: ")
  users.append(profile)
  print("user added")

def show_users():
  if not users:
    print("No users yet.")
    return

  print("\n--- Users ---")
  for user in users:
    print(user)

while True:
  print("\n1. Add User")
  print("2. Show users")
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
    print("Invalid Choice.")
def get_non_empty_input(prompt):
  pass

def get_valid_age():
  pass

def create_profile():
  profile = {}

  name = input("Enter your name: ").strip()
  while not name:
    print("Name cannot be empty. Try again.")
    name = input("Enter your name: ").strip()
    profile["name"] = str(name)
  while True:
    age = input("Enter your age: ")
    if not age.isdigit():
      print("Please enter a number for age. ")
      continue
    age = int(age)

    if age < 1 or age > 120:
      print("Age must be between 1 and 120.")
      continue
    profile["age"] = int(age)
    break
  city = input("Enter your City: ").strip()
  while not city:
    print("City cannot be empty: ")
    city = input("Enter your city: ")
    profile["city"] = str(city)

  return profile


def display_profile(profile):
  print("\n--- User Profile ---")
  for key, value in profile.items():
    print(f"{key.capitalize()}: {value}")

user_profile = create_profile()
display_profile(user_profile)
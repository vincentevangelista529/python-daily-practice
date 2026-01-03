def create_profile():
  profile = {}

  profile["name"] = input("Enter your name: ")
  age = input("Enter your age: ")
  while not age.isdigit():
    age = input("Please enter a number for age: ")
  profile["age"] = int(age)
  profile["city"] = input("Enter your city: ")
  hobby = input("Enter your hobby: ")
  profile["hobby"]= hobby
 
  return profile

def display_profile(profile):
  print("\n--- User Profile ---")
  for key, value in profile.items():
    print(f"{key.capitalize()}: {value}")

user_profile = create_profile()
display_profile(user_profile)

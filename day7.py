data = {}

data["username"] = input("Enter your username: ")
data["email"] = input("Enter your email: ")
data["password"] = input("Enter your password: ")

for key, value in data.items():
  print(f"{key}: {value}")
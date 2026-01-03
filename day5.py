#Problem #1
def greet_user(name):
  print(f"Hello, {name}!")

greet_user("Vincent")
greet_user("Tet")
greet_user("Zel")

#problem #2
def multiply(a, b):
  return a * b

result = multiply(2, 5)
print("The product is: ", result)

#problem #3
def check_even(number):
  if number % 2 == 0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")

check_even(4)
check_even(5)
check_even(6)
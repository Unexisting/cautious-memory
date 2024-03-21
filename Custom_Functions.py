def greet_user():
    print("Please enter your name")
    name = input()
    print("Hello ", name)

users = 5
for user in range(users):
     greet_user()
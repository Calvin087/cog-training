# ctrl alt m - terminate code runner
print("\n") # formatting


users = [
    (0, "Bob", "password"),
    (1, "Dave", "someg276"),
    (2, "Sam", "long687uhb"),
    (3, "Tom", "Copsm129^.")
] # List of Tuples.

username_mapping = {z[1] : z for z in users}

user_name_input = input("Enter username: ")
user_passw_input = input("Enter password: ")

_, username, password = username_mapping[user_name_input]
# Users input then gives me a key to search the dictionary by.

if user_passw_input == password:
    print(f"Thank you {user_name_input}, correct pw")
else:
    print(f"You're not {user_name_input} Imposter!")

print("\n") # formatting
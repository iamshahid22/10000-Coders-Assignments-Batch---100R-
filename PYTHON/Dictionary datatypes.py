# Initialize an empty dictionary to store user profiles
user_profiles = {}

# Function to add a new user profile
def add_user(user_id, name):
    user_profiles[user_id] = name
    print(f"Added User: {user_id} -> {name}")
    print("Dictionary:", user_profiles)
    print()

# Function to retrieve a user's name by ID
def get_user(user_id):
    if user_id in user_profiles:
        print(f"User found: {user_id} -> {user_profiles[user_id]}")
    else:
        print(f"User ID {user_id} not found.")
    print("Dictionary:", user_profiles)
    print()

# Function to update an existing user's name
def update_user(user_id, new_name):
    if user_id in user_profiles:
        user_profiles[user_id] = new_name
        print(f"Updated User ID {user_id} with new name '{new_name}'")
    else:
        print(f"User ID {user_id} not found.")
    print("Dictionary:", user_profiles)
    print()

# Function to remove a user profile by ID
def remove_user(user_id):
    if user_id in user_profiles:
        del user_profiles[user_id]
        print(f"Removed User ID {user_id}")
    else:
        print(f"User ID {user_id} not found.")
    print("Dictionary:", user_profiles)
    print()

# Testing the functions

print("Initial Dictionary:", user_profiles)
print()

# Add users
add_user(101, "Shahid")
add_user(102, "Rahul")
add_user(103, "Ayesha")

# Retrieve users
get_user(102)
get_user(999)  # Not found

# Update user
update_user(103, "Aisha")
update_user(999, "Ali")  # Not found

# Remove user
remove_user(101)
remove_user(999)  # Not found

# Final dictionary
print("Final Dictionary:", user_profiles)

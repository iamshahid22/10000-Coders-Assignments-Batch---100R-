# intialize an empty dictionary
users = {}

#fuction to add  new user
def add_user(id,name):
    users[id] = name
    print("Added ID:",name)
    
#function to retrieve user name by id
def get_user(id):
    names = users.get(id,"user not found")
    print(f"Retrieving ID {id} : {names}")
    return names

#fun to update an existing user name
def update_user(id,new_name):
    if id in users:
        users[id]=new_name
        print(f"Updated ID{id} to :{new_name}")
    else:
        print(f"Error:ID{id} not found.cannot update.")

#fun to remove a user by id
def remove_user(id):
    if id in users:
        removed_name=users.pop(id)
        print(f"Removed ID {id}: {removed_name}")
    else:
        print(f"Error: ID {id} not found. cannot remove.")
    
# test each function
add_user(101,"Shahid")
add_user(102,"venu")

print("Current Profiles:",users)

get_user(101)
get_user(103)

update_user(102,"Keerthi")
update_user(103,"Shyam")

remove_user(102)
remove_user(105)

print("Final Profiles:", users)



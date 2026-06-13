# Creating new list with city names 
cities = ["Kurnool","Tirupati","Hyderabad","Bengaluru","Thaoland"]
print(cities)

#  Use indexing to access and print the name of the city at the middle index of the list
print(cities[2])

# Use slicing to extract a subset of cities from the list
print(cities[0:3])

# Sort the list of cities in ascending order and print the result
cities.sort()
print(cities) 

#  Append a new city to the end of the list and print the updated list
cities.append("Turkey")
print(cities)

# Remove the first city from the list and print the updated list
cities.pop(0)
print(cities)

# Write a function that takes a list of cities as input and returns the length of the list
def list_length(input_list):
    return len(input_list)

#Test the function with the list of cities created in the first task and print the result
length = list_length(cities)
print(length)


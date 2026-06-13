# 1. Create a tuple containing the names of 5 different cities
cities_tuple = ("Kurnool", "Hyderabad", "Bengaluru", "Chennai", "Mumbai")
print("Cities tuple:", cities_tuple)

# 2. Function to return the first and last elements
def get_first_and_last(tup):
    return tup[0], tup[-1]

first, last = get_first_and_last(cities_tuple)
print("First city:", first)
print("Last city:", last)

# 3. Create a tuple of tuples (student names and grades)
students = (("John", 85), ("Alice", 92), ("Bob", 78), ("David", 88))
print(students)

# 4. Function to sort students by name
def sort_students(student):
    return tuple(sorted(student, key=lambda x: x[0]))

sorted_students = sort_students(students)
print(sorted_students)

# 5. Function to practice tuple unpacking
def fruits(tup):
    if len(tup) != 3:
        print("Tuple must have exactly 3 elements")
        return
    
    a, b, c = tup
    print(a,b,c)

three_fruits = ("Apple", "Banana", "Cherry")
fruits(three_fruits)
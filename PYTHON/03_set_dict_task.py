<<<<<<< HEAD
# SET OPERATIONS 
print("--- Set Operations Test ---")
# 1. Create a set from a list to get unique numbers
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(f"Unique Set: {numbers}")

# 2. Add an element
numbers.add(6)

# 3. Remove an element safely
numbers.discard(2)

# 4. Perform set math operations with another set
other_set = {4, 5, 6, 7}
print(f"Union: {numbers | other_set}")
print(f"Intersection: {numbers & other_set}")
print(f"Difference: {numbers - other_set}\n")


#  DICTIONARY LIBRARY SYSTEM
# This dictionary will store your database in memory
library = {}

def add_book(title, author, year, genre):
    library[title] = {
        "Author": author,
        "Year": year,
        "Genre": genre
    }
    print(f"Added: {title}")

def remove_book(title):
    if title in library:
        del library[title]
        print(f"Removed: {title}")
    else:
        print(f"'{title}' not found.")

def search_books(query):
    query = query.lower()
    results = []
    for title, info in library.items():
        if (query in title.lower() or 
            query in info["Author"].lower() or 
            query in info["Genre"].lower()):
            results.append((title, info))
    return results

def display_books(sort_by="title"):
    if not library:
        print("Library is empty.")
        return
        
    if sort_by.lower() == "author":
        sorted_list = sorted(library.items(), key=lambda item: item[1]["Author"].lower())
    else:
        sorted_list = sorted(library.items())
        
    print(f"\n--- Library Catalog (Sorted by {sort_by}) ---")
    for title, info in sorted_list:
        print(f"Title: {title} | Author: {info['Author']} | Genre: {info['Genre']}")


# TEST VERIFICATION SYSTEM
print("--- Library System Test ---")
# Add sample inputs
add_book("Rich dad poor dad", "F. Scott Fitzgerald", 1925, "Fiction")
add_book("1984", "George Orwell", 1949, "Dystopian")
add_book("Animal Farm", "George Orwell", 1945, "Satire")

# Verify sorting requirements
display_books(sort_by="title")
display_books(sort_by="author")

# Verify searching criteria matches
print("\nSearching for 'Orwell':")
for title, info in search_books("Orwell"):
    print(f"- Found {title}")

# Verify structural delete modifications
print()
remove_book("1984")
=======
# SET OPERATIONS 
print("--- Set Operations Test ---")
# 1. Create a set from a list to get unique numbers
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(f"Unique Set: {numbers}")

# 2. Add an element
numbers.add(6)

# 3. Remove an element safely
numbers.discard(2)

# 4. Perform set math operations with another set
other_set = {4, 5, 6, 7}
print(f"Union: {numbers | other_set}")
print(f"Intersection: {numbers & other_set}")
print(f"Difference: {numbers - other_set}\n")


#  DICTIONARY LIBRARY SYSTEM
# This dictionary will store your database in memory
library = {}

def add_book(title, author, year, genre):
    library[title] = {
        "Author": author,
        "Year": year,
        "Genre": genre
    }
    print(f"Added: {title}")

def remove_book(title):
    if title in library:
        del library[title]
        print(f"Removed: {title}")
    else:
        print(f"'{title}' not found.")

def search_books(query):
    query = query.lower()
    results = []
    for title, info in library.items():
        if (query in title.lower() or 
            query in info["Author"].lower() or 
            query in info["Genre"].lower()):
            results.append((title, info))
    return results

def display_books(sort_by="title"):
    if not library:
        print("Library is empty.")
        return
        
    if sort_by.lower() == "author":
        sorted_list = sorted(library.items(), key=lambda item: item[1]["Author"].lower())
    else:
        sorted_list = sorted(library.items())
        
    print(f"\n--- Library Catalog (Sorted by {sort_by}) ---")
    for title, info in sorted_list:
        print(f"Title: {title} | Author: {info['Author']} | Genre: {info['Genre']}")


# TEST VERIFICATION SYSTEM
print("--- Library System Test ---")
# Add sample inputs
add_book("Rich dad poor dad", "F. Scott Fitzgerald", 1925, "Fiction")
add_book("1984", "George Orwell", 1949, "Dystopian")
add_book("Animal Farm", "George Orwell", 1945, "Satire")

# Verify sorting requirements
display_books(sort_by="title")
display_books(sort_by="author")

# Verify searching criteria matches
print("\nSearching for 'Orwell':")
for title, info in search_books("Orwell"):
    print(f"- Found {title}")

# Verify structural delete modifications
print()
remove_book("1984")
>>>>>>> a654b49 (python task added)
display_books(sort_by="title")
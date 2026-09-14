"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
    print("Example: checking whether library books are available.")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # Original prompt: TODO: Create a dictionary and add multiple key-value pairs.
    # I used the dictionary operations from zyBooks section 18.1.
    # Each book ID is a key, and its availablity is the value.
    # A dictonary uses hashing to help locate a value using its key.
    books = {}
    books[101] = "Available"
    books[102] = "Checked out"
    books[103] = "Available"
    books[104] = "Checked out"
    books[105] = "Available"
    print("Library books:", books)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Original prompt: TODO: Demonstrate successful key lookups.
    # The key is used to find the book's value without scaning every book.
    print("Book 101:", books[101])
    print("Book 102:", books[102])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    # Original prompt: TODO: Demonstrate updating an existing key.
    print("Before book 102 was returned:", books)
    # Assigning to the same key replces its value, so no extra book is added.
    books[102] = "Available"
    print("After book 102 was returned:", books)
    print("Number of books after the update:", len(books))

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # Original prompt: TODO: Demonstrate deleting a key-value pair.
    print("Before removing book 104:", books)
    # del removes both the book ID and its assocaited value.
    del books[104]
    print("After removing book 104:", books)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Original prompt: TODO: Demonstrate and explain edge cases.
    # get returns the mesage when the key is missing, avoiding a KeyError.
    print("Missing book 999:", books.get(999, "Book not found"))

    # Checking for the key first prevents deletng a book that is not there.
    if 999 in books:
        del books[999]
    else:
        print("Cannot delete book 999 because it is not in the dictionary.")

    # An emtpy dictionary has no books, so this also returns the message.
    empty_books = {}
    print("Book 101 in an empty dictionary:",
          empty_books.get(101, "Book not found"))

    # zyBooks 8.2 explains that diffrent keys can map to the same bucket.
    # Chaining keeps a list in that bucket. Open addressing finds another bucket.
    # The dictionary handles collisions internally; I did not write that code.
    # More collisions can mean more checks when looking for a book.



if __name__ == "__main__":
    main()

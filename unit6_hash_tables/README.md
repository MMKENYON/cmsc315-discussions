# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## What I Did

I used a dictionary to track library books. Each book ID was a key, and its
value was either "Available" or "Checked out". I followed the basic dictionary
operations in zyBooks section 18.1 and the hashing explanations in sections
8.2 and 18.2. I kept the starter prompts and comments.

I added five books and looked up books 101 and 102. I changed book 102 to
"Available" when it was returned. The dictionary still had five books because
the update replaced a value for an existing key. I then removed book 104.

## Results

- Book 101 was available, and book 102 was checked out before the update.
- Updating book 102 changed its value to "Available".
- Deleting book 104 left four books in the dictionary.
- Looking up missing book 999 displayed "Book not found".
- Trying to delete book 999 displayed a message and left the dictionary alone.
- Looking up book 101 in an empty dictionary displayed "Book not found".

I used `get()` for the missing lookups and checked `if 999 in books` before
trying to delete it. These checks avoided a `KeyError`.

## Hash Tables and Collisions

I learned that a hash function helped locate a key in a hash table. Different
keys could map to the same bucket, which caused a collision. The textbook
described chaining, which kept a list at each bucket, and open addressing,
which looked for another bucket. I used Python's dictionary, which handled
collisions internally. I did not implement a collision-handling algorithm.

More collisions meant more checks during a search. With a good hash function,
lookups took O(1) expected time. In the worst case, they could take O(n) time.
I explained this using the textbook; I did not measure lookup times.

## How I Ran It

From the main project folder, I ran:

```text
python3 unit6_hash_tables/unit6_discussion.py
```

## My Reflection

For this assignment, I used a Python dictionary to keep track of library books.
Each book ID was a key, and its value showed whether the book was available
or checked out. I added five books, looked up two, updated one, and removed
another.

The part I checked carefully was looking up or deleting a book that was not
there. I used get() to show "Book not found" and an if statement before
deleting a missing key. I also tested an empty dictionary. The program showed
a message instead of stopping with an error.

I learned that a hash table uses a hash function to help find where a key
belongs. A collision happens when different keys map to the same bucket.
Chaining keeps those entries in a list, while open addressing looks for
another bucket. Python handled collisions inside the dictionary. More
collisions can slow down searches because more entries need to be checked.
With a good hash function, lookups usually take O(1) time, which helps when
finding a book in a large collection.

## Textbook Sources

- [8.2 Hash tables](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/8/section/2)
- [18.1 Maps and dictionaries](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/18/section/1)
- [18.2 Hash tables](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/18/section/2)

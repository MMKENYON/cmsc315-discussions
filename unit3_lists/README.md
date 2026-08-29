# Unit 3 Discussion: List Operations

## Overview

I created a small course assignment tracker using a Python list. The program
demonstrated insertion, deletion, and searching.

## Program Design

The program used a list named `assignments`. Each item in the list represented
a school assignment.

I created three functions:

- `insert_at` inserted an assignment.
- `delete_at` removed and returned an assignment.
- `search_value` searched for an assignment.

## Operations Tested

I tested insertion at the beginning, middle, and end of the list. I also tested
deletion from all three positions.

The search tests included an assignment that was in the list and one that was
missing. The two edge cases were deleting from an invalid index and deleting
from an empty list.

## List Performance

Python lists are array-based. Inserting or deleting near the beginning or
middle may cause other items to shift. Operations near the end usually require
less shifting.

A linked list may work better when a program frequently adds or removes items
near the beginning or middle. It can reconnect its nodes without shifting every
later item.

## Real-World Scenario

A list could be used to organize school assignments. A student could insert a
new assignment, remove a completed assignment, or search for an assignment.

## Reflection

While completing this assignment, I learned how Python lists can be changed by
inserting, deleting, and searching for values. I used `insert()` to add
assignments at the beginning, middle, and end of the list. I used `pop()` to
remove an assignment and return the removed value. I also wrote a linear search
that checked each item in order until it found a match.

One challenge was keeping track of the indexes after the list changed. When an
item was inserted or deleted, the positions of later items changed too. I
handled this by printing the list after every operation and checking its current
length before deleting the last item. I also checked indexes before deletion so
an invalid index would return `None` instead of stopping the program.

This project showed me that list performance depends on where an operation
happens. Adding or removing an item near the beginning or middle may require
other items to shift. Operations near the end usually require less shifting.

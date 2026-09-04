# Unit 4 Discussion: Binary Search Trees

## Overview

I made a binary search tree for book ID numbers in a library. The program adds
book IDs, searches for them, and displays them in order.

## What I Did

Each node stores one number and has a place for a left child and a right child.
When a number is smaller than the current node, it goes left. When it is larger,
it goes right. I used recursion for inserting, searching, and visiting the tree.

I inserted seven book IDs so the tree had values on both sides. The in-order
traversal displayed the IDs from smallest to largest. I also searched for two
IDs that were in the tree and two IDs that were not in the tree.

## Edge Case

I used an empty tree as my edge case. Its traversal returned an empty list, and
searching it returned `False` instead of causing an error.

## Efficiency

A binary search tree uses its ordering to decide whether to go left or right.
This can make searching faster than checking every item in a regular list.
However, the tree works best when it is balanced. If it becomes one long side,
searching can take more steps.

## Discussion Board Reflection

While doing this assignment, I learned that a binary search tree keeps values
organized by comparing them with the current node. A smaller value goes to the
left, and a larger value goes to the right. I also learned how recursion can be
used to keep moving through the tree until the program finds an empty place or
the value it is looking for.

The hardest part for me was following the recursive calls. At first, I was not
sure how the program returned to the earlier nodes. I worked through the values
one at a time and drew a small tree on paper. That made the left and right
branches easier to understand. I also tested an empty tree to make sure the
program did not cause an error.

A binary search tree can be faster than searching a regular list because its
ordering tells the program which direction to go. A list search may have to
check every item. A tree can still become slow if all its values go to one side,
so the way the tree is shaped affects how efficient it is.

## How to Run

From the main project folder, run:

```text
python3 unit4_trees/unit4_discussion.py
```

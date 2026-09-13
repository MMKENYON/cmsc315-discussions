# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

### My Reflection

For this assignment, I made a program that searched for library book IDs. I used the search steps from zyBooks sections 7.1 and 7.2 and wrote them in Python. Linear search checked each book ID in order. Binary search checked the middle ID and then searched the left or right half of the sorted list.

I tested a list of five books and a list of 1,000 books. Both searches found the requested book or returned -1 when it was missing. I also tested an empty list, a list with one book, and the first and last books.

The part I checked carefully was moving low and high past the middle position. This kept binary search from checking the same position again.

I learned that linear search had O(n) worst-case time because it might check every item. Binary search had O(log n) time because it kept cutting the search area in half. Linear search was useful for one lookup in an unsorted pile of returned books. Sorting that pile first would add work. Binary search was useful for repeated searches, but it needed the IDs sorted in order.

## What I Did

I used the Java search examples in zyBooks sections 7.1 and 7.2 as a guide
and adapted their steps into Python. I kept the starter function names and
assignment prompts. I used lists, loops, if statements, and print statements.

## Results

| Test | Linear result | Binary result |
| --- | --- | --- |
| Five books: find 30 | 2 | 2 |
| Five books: find missing 35 | -1 | -1 |
| 1,000 books: find 1000 | 999 | 999 |
| 1,000 books: find missing 1001 | -1 | -1 |
| Empty list | -1 | -1 |
| One book [25]: find 25 | 0 | 0 |
| One book [25]: find missing 30 | -1 | -1 |
| First book in the small list | 0 | 0 |
| Last book in the small list | 4 | 4 |

Both searches returned the expected index, or -1 for a missing ID.
For the two large-list targets, linear search visited all 1,000 items.
Binary search visited 10 items because it kept cutting the list in half.
This compared search steps, not measured running time. For a match at the
first position, linear search needed only one check.

I also searched an unsorted return list, [40, 10, 30]. Linear search found
book 30 at index 2. I did not use binary search on that list because the IDs
were not sorted. Sorting first would add work. I used integer book IDs so
the values could be compared in order.

## How I Ran It

From the main project folder, I ran:

```text
python3 unit5_searching_analysis/unit5_discussion.py
```

I saved the program's output in [sample_output.txt](sample_output.txt).

## zyBooks Sources

I adapted the search algorithms from
[7.1 Searching and algorithms](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/7/section/1) and
[7.2 Binary search](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/7/section/2). The book examples used Java;
this discussion required Python. I added the library example and test lists.

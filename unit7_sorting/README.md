# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## What I Did

I used returned library book IDs as my example. I followed the Bubble Sort
steps in zyBooks section 9.2 and the Merge Sort steps in section 9.6. I wrote
the steps in Python using the starter functions and kept the original prompts
and comments.

Bubble Sort copied the list, compared neighboring values, and swapped them
when needed. Merge Sort split the list into halves until each part had at
most one value. The merge function compared the two sorted halves and added
their values to a new list. Both sorts left the original lists unchanged.

## Results

- Dataset 1 had seven book IDs. Both sorts returned
  `[101, 102, 103, 104, 105, 106, 107]`.
- Dataset 2 had eight different book IDs. Both sorts returned
  `[201, 202, 203, 204, 205, 206, 207, 208]`.
- Both sorts returned `[]` for an empty list.
- Both sorts returned `[301]` for the list with one book.

## Efficiency and Tradeoffs

I compared the algorithms using the textbook's time complexity explanations.
Bubble Sort used O(n²) time because it used nested loops. This version still
made all its comparisons if the list was already sorted. Merge Sort used
O(n log n) time because it had about log n levels and did O(n) work at each
level. Its work grew more slowly as the number of books increased.

Merge Sort used extra lists for splitting and merging. Bubble Sort worked
within its copy, but that required copy also used O(n) extra space. Merge Sort
used O(n) extra space overall. I used the textbook analysis rather than
measuring run times for these small lists.

## How I Ran It

From the repository folder, I ran:

```text
python3 unit7_sorting/unit7_discussion.py
```

## My Reflection

For this assignment, I wrote a program that sorted library book IDs using Bubble Sort and Merge Sort. Bubble Sort compared neighboring values and swapped them when they were out of order. Merge Sort divided the list into halves, sorted each half, and merged them back together.

I tested two unsorted lists, an empty list, and a list with one book. Both algorithms returned the same sorted results. The part I checked carefully was finishing the merge when one half ran out of values. I used while loops to add the values left in the other half.

I learned that Bubble Sort used O(n²) time because of its nested loops. Merge Sort used O(n log n) time because it divided the problem into smaller parts and merged each level. Its work grew more slowly as the list got larger. The tradeoff was the extra lists used during merging.

I would use Bubble Sort for a small practice list because its steps were easy to follow. I would choose Merge Sort to put a large collection of returned library book IDs in order.

## Textbook Sources

- [zyBooks 9.2: Bubble sort](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/9/section/2)
- [zyBooks 9.6: Merge sort](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/9/section/6)

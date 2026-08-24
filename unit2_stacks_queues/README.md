# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two linear data structures:

- Stack using Last-In, First-Out (LIFO)
- Queue using First-In, First-Out (FIFO)

## Design and Scenario

I implemented the stack with a Python list and the queue with `collections.deque`. My program used a library scenario. The stack represented returned books placed on top of one another. The last book placed on the stack was the first book removed. The queue represented patrons waiting for library holds. The first patron added was the first patron processed.

## Work Completed

I completed every required section in the Python file. I implemented `push`, `pop`, `peek`, and `is_empty` for the stack. I also implemented `enqueue`, `dequeue`, `front`, and `is_empty` for the queue. I added clear output, comments, empty-structure tests, single-item tests, and additional mixed-operation tests.

## Edge Cases

The program checked whether each structure was empty before removing or viewing a value. Empty operations printed a message and returned `None` instead of causing an error. I also verified that removing the only item from a stack or queue made the structure empty.

## Memory Use

The stack and queue used `O(n)` memory because each added item required another stored reference. Their memory use grew in proportion to the number of items currently stored and decreased as items were removed.

## Discussion Board Reflection

While completing this assignment, I learned that stacks and queues can use similar operations but organize information in different orders. The stack used a Python list because adding and removing from the end worked well for LIFO. The queue used `deque` because `popleft()` removed the oldest item efficiently for FIFO. My library example helped me understand the difference. Returned books were placed on top of a stack, so the newest book was removed first. Library hold requests were handled in the order patrons joined the queue.

The main challenge was deciding what should happen when the program tried to remove or view an item from an empty structure. Without a check, those operations could cause an error. I used `is_empty()` before `pop`, `peek`, `dequeue`, and `front`. The methods printed a simple message and returned `None` when no value was available. I also tested a structure containing only one item and confirmed it became empty after removal. This assignment showed me that small edge-case checks can make a program safer and easier to understand.

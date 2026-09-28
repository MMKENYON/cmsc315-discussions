# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

### My Reflection

For this assignment, I made a graph of six people and their friendships using an adjacency list. I followed the BFS steps in zyBooks section 10.8. A queue visited Amy first, then her direct friends, and then people farther away. This helped me understand how BFS worked one level at a time.

The part I had to watch was keeping people from being added more than once. I marked each person as visited when I added them to the queue. I added a friendship between Amy and Finn, which moved Finn earlier in the traversal. I tested a disconnected person and a missing starting name. The disconnected person was skipped, and the missing name returned an empty list.

BFS would be useful for suggesting friends of friends because it checked closer connections first. DFS used a stack and followed one path before going back to try another. I would choose DFS for exploring a maze when I only needed a path to the exit. I would choose BFS when I needed the path with the fewest edges in an unweighted graph.

## How I Ran It

From the main project folder, I ran:

```text
python3 unit8_graphs/unit8_discussion.py
```

The first traversal returned Amy, Ben, Cara, Dan, Eva, Finn.
After I connected Amy and Finn, it returned Amy, Ben, Cara, Finn, Dan, Eva.
Adding Zoe without connections left the traversal from Amy unchanged.
Starting from the missing name Leo returned `[]`.

## Sources

I used the BFS steps in
[zyBooks 10.8](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/10/section/8)
as a guide and wrote them in Python. I used
[zyBooks 10.9](https://learn.zybooks.com/zybook/CMSC__315_6300_Data_Structures_and_Analysis_(2268)/chapter/10/section/9)
for the DFS comparison.

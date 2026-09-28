"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # I followed the BFS steps in zyBooks section 10.8.
    # A missing starting name has no nodes to visit.
    if start not in graph:
        return []

    visited = set()
    order = []
    queue = deque()
    queue.append(start)
    visited.add(start)

    # A queue removes the first node added, so closer nodes go frist.
    # DFS follows one path deeper before going back to other paths.
    while queue:
        node = queue.popleft()
        order.append(node)

        # Add neighbors so thier connections can be checked later.
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark the neighbor now so it is not added twice.
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    # Original prompt: TODO: Create and display a graph.
    # Each node was a person, and each edge was a friendship.
    # Friendships went both ways, so both names listed eachother.
    graph = {
        "Amy": ["Ben", "Cara"],
        "Ben": ["Amy", "Dan", "Eva"],
        "Cara": ["Amy", "Eva"],
        "Dan": ["Ben", "Finn"],
        "Eva": ["Ben", "Cara", "Finn"],
        "Finn": ["Dan", "Eva"]
    }

    for person in graph:
        print(person, "is connected to:", graph[person])

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    # Original prompt: TODO: Perform and explain BFS traversal.
    # Amy was first, followed by Ben and Cara, then Dan and Eva,
    # and finally Finn. Each group was one more edge from Amy.
    print("Starting person: Amy")
    print("BFS order:", bfs(graph, "Amy"))
    print("BFS visited Amy, her friends, and then people farther away.")

    # I added one friendship between Amy and Finn in both directions.
    graph["Amy"].append("Finn")
    graph["Finn"].append("Amy")
    print("\nAdded a friendship between Amy and Finn.")
    print("Updated BFS order:", bfs(graph, "Amy"))
    print("Finn was now a direct friend, so BFS visited him before Dan and Eva.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Original prompt: TODO: Demonstrate and explain edge cases.
    # Zoe had no connections, so BFS from Amy could not reach her.
    graph["Zoe"] = []
    print("Disconnected graph: added Zoe with no friends.")
    print("BFS from Amy:", bfs(graph, "Amy"))
    print("Zoe was not visited because no path connected Amy to Zoe.")

    # Leo was not a node in the graph, so the function returned [].
    print("\nMissing starting person: Leo")
    print("BFS from Leo:", bfs(graph, "Leo"))
    print("The result was an empty list because Leo was not in the graph.")



if __name__ == "__main__":
    main()

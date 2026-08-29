"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the requested index.
    # Later items shift one position to the right.
    # Beginning and middle insertions take more work than the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check the index so the program does not crash.
    # This also makes deletion safe when the list is empty.
    if index >= 0 and index < len(lst):
        return lst.pop(index)

    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because it checks each item in order.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    assignments = [
        "Read chapter",
        "Write discussion",
        "Complete lab"
    ]
    print("Original list:", assignments)

    # Add an assignment at the beginning.
    insert_at(assignments, 0, "Check announcements")
    print("After adding at the beginning:", assignments)

    # Add an assignment in the middle.
    insert_at(assignments, 2, "Review notes")
    print("After adding in the middle:", assignments)

    # Add an assignment at the end.
    insert_at(assignments, len(assignments), "Submit work")
    print("After adding at the end:", assignments)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    removed = delete_at(assignments, 0)
    print("Removed from the beginning:", removed)
    print("Updated list:", assignments)

    removed = delete_at(assignments, 2)
    print("Removed from the middle:", removed)
    print("Updated list:", assignments)

    last_index = len(assignments) - 1
    removed = delete_at(assignments, last_index)
    print("Removed from the end:", removed)
    print("Updated list:", assignments)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    found_index = search_value(assignments, "Review notes")
    print("Index of Review notes:", found_index)

    missing_index = search_value(assignments, "Take quiz")
    print("Index of Take quiz:", missing_index)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    invalid_result = delete_at(assignments, 20)
    print("Invalid deletion:", invalid_result)

    empty_assignments = []
    empty_result = delete_at(empty_assignments, 0)
    print("Empty list deletion:", empty_result)



if __name__ == "__main__":
    main()

"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Based on the linear search steps in zyBooks section 7.1.
    # Check each item from the begining of the list.
    # In the worst case, all n items are checked, so the time is O(n).
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Based on the binary search steps in zyBooks section 7.2.
    # The list must be sorted from smallest to largest.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] < target:
            low = mid + 1       # Search the right half.
        elif lst[mid] > target:
            high = mid - 1      # Search the left half.
        else:
            return mid

    # Each step cuts the remaining search area about in half: O(log n).
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Example: searching for library book IDs.")
    print("An index starts at 0. A result of -1 means not found.")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # Original prompt: TODO: Create a small dataset and test both searches.
    books = [10, 20, 30, 40, 50]
    print("Book IDs:", books)

    # Book 30 is at index 2. Both searches should return 2.
    print("Search for book 30:")
    print("Linear:", linear_search(books, 30))
    print("Binary:", binary_search(books, 30))

    # Book 35 is misssing. Both searches should return -1.
    print("Search for missing book 35:")
    print("Linear:", linear_search(books, 35))
    print("Binary:", binary_search(books, 35))
    print("Both found book 30 and returned -1 for missing book 35.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Original prompt: TODO: Create a larger dataset and compare results.
    large_books = list(range(1, 1001))
    print("This list has 1,000 book IDs, from 1 to 1000.")

    # Book 1000 is the last item, at index 999.
    print("Search for book 1000:")
    print("Linear:", linear_search(large_books, 1000))
    print("Binary:", binary_search(large_books, 1000))

    # Book 1001 is not in the list.
    print("Search for missing book 1001:")
    print("Linear:", linear_search(large_books, 1001))
    print("Binary:", binary_search(large_books, 1001))

    # Tracing these searches gives 1,000 visited items for linear search
    # and 10 for binary search. This explians the work, not elapsed time.
    print("Both searches gave the same results.")
    print("For these targets, linear search checks all 1,000 items.")
    print("Binary search checks 10 items by cutting the search area in half.")
    print("This saves more work as the sorted list gets larger.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Original prompt: TODO: Demonstrate and explain edge cases.

    # An emtpy list has no items to search, so both return -1.
    print("Empty list: both should return -1.")
    print("Linear:", linear_search([], 10))
    print("Binary:", binary_search([], 10))

    # The only item is at index 0.
    print("One item [25], search for 25: both should return 0.")
    print("Linear:", linear_search([25], 25))
    print("Binary:", binary_search([25], 25))

    # A single-item list can also have a missing valeu.
    print("One item [25], search for 30: both should return -1.")
    print("Linear:", linear_search([25], 30))
    print("Binary:", binary_search([25], 30))

    # Check the first and last postions in the small list.
    print("First book 10: both should return 0.")
    print("Linear:", linear_search(books, 10))
    print("Binary:", binary_search(books, 10))
    print("Last book 50: both should return 4.")
    print("Linear:", linear_search(books, 50))
    print("Binary:", binary_search(books, 50))

    # Returned books may not be sorted. Linear seach still works.
    returned_books = [40, 10, 30]
    print()
    print("Unsorted returned books:", returned_books)
    print("Linear search for book 30:", linear_search(returned_books, 30))
    print("Binary search needs the book IDs to be sorted first.")


if __name__ == "__main__":
    main()

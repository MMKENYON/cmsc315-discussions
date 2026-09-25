"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Copy the list so the original book IDs stay in the same order.
    numbers = lst.copy()

    # Follow the nested loops in zyBooks section 9.2.
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            # Swap neighboring values if they are out of order.
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # An empty list or a list with one value is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Follow the split, sort, and merge steps in zyBooks section 9.6.
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = 0
    j = 0

    # Add the smaller value and move forward in that list.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    # Add any values left after the other list runs out.
    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")
    print("Example: putting returned library book IDs in order.")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    # Original prompt: TODO: Create an unsorted dataset and test both sorting algorithms.
    books = [107, 103, 101, 106, 102, 105, 104]
    print("Original book IDs:", books)
    bubble_result = bubble_sort(books)
    merge_result = merge_sort(books)
    print("Bubble Sort:", bubble_result)
    print("Merge Sort:", merge_result)
    print("Results match:", bubble_result == merge_result)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    # Original prompt: TODO: Create a second dataset and compare sorting results.
    more_books = [208, 203, 206, 201, 207, 204, 202, 205]
    print("Original book IDs:", more_books)
    bubble_result = bubble_sort(more_books)
    merge_result = merge_sort(more_books)
    print("Bubble Sort:", bubble_result)
    print("Merge Sort:", merge_result)
    print("Results match:", bubble_result == merge_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Original prompt: TODO: Demonstrate and explain edge cases.
    print("Empty list:")
    print("Bubble Sort:", bubble_sort([]))
    print("Merge Sort:", merge_sort([]))
    print("Both returned an empty list because there were no values to sort.")

    print("\nOne book [301]:")
    print("Bubble Sort:", bubble_sort([301]))
    print("Merge Sort:", merge_sort([301]))
    print("Both returned [301] because one value was already sorted.")

if __name__ == "__main__":
    main()

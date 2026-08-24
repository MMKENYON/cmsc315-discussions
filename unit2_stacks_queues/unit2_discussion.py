from collections import deque


class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        # Appending places the newest value at the top so it can be removed first.
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            print("The stack is empty, so there is nothing to remove.")
            return None
        return self.values.pop()

    def peek(self):
        # Peek lets the program view the newest value without changing the stack.
        if self.is_empty():
            print("The stack is empty, so there is no top value to view.")
            return None
        return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0


class Queue:
    def __init__(self):
        self.values = deque()

    def enqueue(self, value):
        # Appending adds each new request behind the requests that arrived earlier.
        self.values.append(value)

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, so there is nothing to remove.")
            return None
        return self.values.popleft()

    def front(self):
        # Front shows the request that has waited the longest without removing it.
        if self.is_empty():
            print("The queue is empty, so there is no front value to view.")
            return None
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("Scenario: A library organizes returned books and hold requests.")

    print("\n=== RETURNED BOOK STACK ===")
    returned_books = Stack()
    books = ["Mystery novel", "Science book", "History book", "Poetry collection"]

    for book in books:
        returned_books.push(book)
        print(f"Placed on top of the return stack: {book}")

    print(f"The top book is: {returned_books.peek()}")
    print("Removing books from the top demonstrates LIFO:")
    while not returned_books.is_empty():
        print(f"  Removed: {returned_books.pop()}")

    print("Trying to pop from the empty stack:")
    returned_books.pop()
    print("Trying to peek at the empty stack:")
    returned_books.peek()

    single_book_stack = Stack()
    single_book_stack.push("Dictionary")
    print(f"Single-item stack removed: {single_book_stack.pop()}")
    print(f"Is the single-item stack empty now? {single_book_stack.is_empty()}")

    print("\n=== LIBRARY HOLD REQUEST QUEUE ===")
    hold_requests = Queue()
    patrons = ["Ava", "Noah", "Mia", "Ethan"]

    for patron in patrons:
        hold_requests.enqueue(patron)
        print(f"Added to the back of the hold-request line: {patron}")

    print(f"The next patron to receive a book is: {hold_requests.front()}")
    print("Processing hold requests in arrival order demonstrates FIFO:")
    while not hold_requests.is_empty():
        print(f"  Processed: {hold_requests.dequeue()}")

    print("Trying to dequeue from the empty queue:")
    hold_requests.dequeue()
    print("Trying to view the front of the empty queue:")
    hold_requests.front()

    single_request_queue = Queue()
    single_request_queue.enqueue("Liam")
    print(f"Single-item queue removed: {single_request_queue.dequeue()}")
    print(f"Is the single-item queue empty now? {single_request_queue.is_empty()}")

    # Additional mixed-operation tests went beyond the starter examples.
    print("\n=== ADDITIONAL MIXED-OPERATION TESTS ===")
    mixed_stack = Stack()
    mixed_stack.push("Atlas")
    mixed_stack.push("Dictionary")
    print(f"Stack test removed: {mixed_stack.pop()}")
    mixed_stack.push("Cookbook")
    print(f"Stack test new top: {mixed_stack.peek()}")

    mixed_queue = Queue()
    mixed_queue.enqueue("Olivia")
    mixed_queue.enqueue("James")
    print(f"Queue test processed: {mixed_queue.dequeue()}")
    mixed_queue.enqueue("Sophia")
    print(f"Queue test next patron: {mixed_queue.front()}")


if __name__ == "__main__":
    main()

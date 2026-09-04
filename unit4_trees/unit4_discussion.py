class Node:
    def __init__(self, value):
        # each node starts with no children
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # the tree starts empty
        self.root = None

    def insert(self, value):
        # start inserting from the root
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # if there is no node here make a new one
        if node is None:
            return Node(value)

        # smaller numbers go left and larger numbers go right
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        # start searching from the root
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True

        # the number tells the program which side to search
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is None:
            return

        # going left then to the node and then right puts the values in order
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    print("\n=== TREE CONSTRUCTION ===")
    print("Scenario: A library stores numeric book IDs in a search tree.")

    library_catalog = BST()
    book_ids = [50, 30, 70, 20, 40, 60, 80]

    # these values make branches on both sides of the root
    for book_id in book_ids:
        library_catalog.insert(book_id)

    print("Book IDs inserted:", book_ids)

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_book_ids = library_catalog.inorder()
    print("Book IDs in sorted order:", sorted_book_ids)
    print("The traversal visited the left subtree, node, and right subtree.")

    print("\n=== SEARCH TESTS ===")
    print("Book ID 20 is in the tree:", library_catalog.search(20))
    print("Book ID 60 is in the tree:", library_catalog.search(60))
    print("Book ID 25 is in the tree:", library_catalog.search(25))
    print("Book ID 90 is in the tree:", library_catalog.search(90))

    print("\n=== EDGE CASES ===")
    empty_catalog = BST()
    print("Empty tree traversal:", empty_catalog.inorder())
    print("Search an empty tree for 50:", empty_catalog.search(50))



if __name__ == "__main__":
    main()

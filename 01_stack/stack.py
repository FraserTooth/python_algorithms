class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adds an item to end
        Returns Nothing

        Time Complexity = O(1)
        """
        self.items.append(item)

    def pop(self):
        """Removes Last Item
        Returns Item

        Time Complexity = O(1)
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns Last Item

        Time Complexity = O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns Size of Stack

        Time Complexity = O(1)
        """
        return len(self.items)

    def is_empty(self):
        """Returns Boolean of whether list is empty

        Time Complexity = O(1)
        """
        return self.items == []

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
        return self.items.pop()

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

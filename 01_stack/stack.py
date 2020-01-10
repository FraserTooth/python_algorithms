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
        pass

    def is_empty(self):
        pass

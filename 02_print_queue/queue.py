class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds item to start of list
        Returns Nothing

        Time Complexity: O(n)
        Adding to the start of a Python list shifts 
        all items along one memory space
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes item from end of the list
        Returns item

        Time Complexity: O(1)
        """
        if self.items:
            return self.items.pop()

    def peek(self):
        """Returns Last Item

        Time Complexity = O(1)
        """
        if self.items:
            return self.items[-1]

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

class Dequeue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Adds to Start

        Time Complexity: O(n) - due to shifting
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """Adds to End

        Time Complexity: O(1)
        """
        self.items.append(item)

    def remove_front(self):
        """Removes First Item

        Time Complexity: O(n) - due to shifting
        """
        if self.items:
            return self.items.pop(0)

    def remove_rear(self):
        """Adds to Start

        Time Complexity: O(1)
        """
        if self.items:
            return self.items.pop()

    def peek_front(self):
        """Check First Item

        Time Complexity: O(1)
        """
        if self.items:
            return self.items[0]

    def peek_rear(self):
        """Check Last Item

        Time Complexity: O(1)
        """
        if self.items:
            return self.items[-1]

    def size(self):
        """Returns Size of List

        Time Complexity: O(1)
        """
        return len(self.items)

    def is_empty(self):
        """Checks if list if Empty

        Time Complexity: O(1)
        """
        return len(self.items) == 0

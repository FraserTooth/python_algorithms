from dequeue import Dequeue

##Must be Solved Using a Dequeue


def PalindromeDetector(string):
    dq = Dequeue()
    for letter in string:
        dq.add_rear(letter)

    while dq.size() > 1:
        if dq.remove_front() != dq.remove_rear():
            return False

    return True

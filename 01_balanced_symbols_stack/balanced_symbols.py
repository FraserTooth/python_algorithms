from stack import Stack

# Must be solved using a Stack


def BalancedSymbols(string):
    keymap = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()
    for symbol in string:
        if symbol in keymap:
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            if keymap[stack.peek()] == symbol:
                stack.pop()

    return stack.is_empty()

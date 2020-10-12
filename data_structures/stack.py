

class Stack:

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return "Top -> {}".format(self._stack[::-1])

    def isEmpty(self):
        return self._stack == []

    def peek(self):
        if self.isEmpty():
            return None
        return self._stack[-1]

    def pop(self):
        if len(self._stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self._stack.append(item)

    def clear(self):
        self._stack = []
        

if __name__ == "__main__":
    s = Stack()

    print(s.isEmpty())
    s.push("pip")
    print(s.isEmpty())

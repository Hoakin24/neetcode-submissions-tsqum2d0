class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = None

    def push(self, val: int) -> None:
        print(val)
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)

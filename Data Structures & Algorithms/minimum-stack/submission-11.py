class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if self.curr_min is None or val <= self.curr_min:
            self.stack.append((val, val))
            self.curr_min = val
        elif val > self.curr_min:
            self.stack.append((val, self.curr_min))
        
        return

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.curr_min = self.getMin()
        else:
            self.curr_min = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


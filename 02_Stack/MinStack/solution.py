# time: O(1)
class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.data[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

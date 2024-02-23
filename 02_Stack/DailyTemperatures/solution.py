from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans

def MonotoicStack(inputs: list[int]) -> list[int]:
    stack = []
    for i in range(len(inputs)):
        while stack and inputs[i] > inputs[stack[-1]]:
            idx = stack.pop()
        stack.append(inputs[i])
    return stack

print(MonotoicStack([1, 2, 5, 3, 4, 6]))
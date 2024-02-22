'''

逆ポーランド記法の式を評価する
1. 数字はスタックに積む
2. 演算子を見つけたらスタックから2つの数字を取り出して計算結果をスタックに積む
3. 最後にスタックに残った数字が結果

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def add(x, y):
            return x + y
        
        def subtract(x, y):
            return x - y
        
        def multiply(x, y):
            return x * y
        
        def divide(x, y):
            return int(x / y)  
        
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
        }
        
        for token in tokens:
            if token in operations:
                x = stack.pop()
                y = stack.pop() 
                operation = operations[token]
                stack.append(operation(x, y))
            else:
                stack.append(int(token))
                
        return stack[0] if stack else 0


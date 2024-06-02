#case1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hp = []
        for token in tokens:
            if token in "+-*/":
                operand2 = hp.pop()
                operand1 = hp.pop()
                if token == "+":
                    hp.append(operand1 + operand2)
                elif token == "-":
                    hp.append(operand1 - operand2)
                elif token == "*":
                    hp.append(operand1 * operand2)
                elif token == "/":
                    hp.append(int(operand1 / operand2))  # Integer division as per the problem description
            else:
                hp.append(int(token))
                  
        return hp[0]

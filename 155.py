
#case1
class MinStack:
    def __init__(self):
        self.stack = []    # Main stack to store elements
        self.min_stack = []  # Stack to store the minimum element at each step

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None  # Handle the case where the stack is empty

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Han
    
#case 2
class MinStack:
    def __init__(self):
        self.stack = []    # Main stack to store elements
        self.min_stack = []  # Stack to store the minimum element at each step

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Example usage:
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Output: 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.getMin())  # Output: 1
print(min_stack.top())      # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 2

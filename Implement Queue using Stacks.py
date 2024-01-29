class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack = []
        while self.stack:
            stack.append(self.stack.pop())
        num = stack.pop()
        while stack:
            self.stack.append(stack.pop())
        return num

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# class MyQueue:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#
#     def pop(self) -> int:
#         temp_stack = []
#         while self.stack:
#             temp_stack.append(self.stack.pop())
#         ans = temp_stack.pop()
#         while temp_stack:
#             self.stack.append(temp_stack.pop())
#         return ans
#
#     def peek(self) -> int:
#         return self.stack[0]
#
#     def empty(self) -> bool:
#         return not self.stack
#
# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()

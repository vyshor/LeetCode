from collections import deque

a = deque()
b = deque(['b', 'cx'])
a.append("a")
print(a)
print(len(a))
print(a+b)
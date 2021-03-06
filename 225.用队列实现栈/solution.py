import collections
# 两个队列的解法
# class MyStack:
#     def __init__(self):
#         self.queue1 = collections.deque()
#         self.queue2 = collections.deque()
#     def push(self, x: int) -> None:
#         self.queue2.append(x)
#         while self.queue1:
#             self.queue2.append(self.queue1.popleft())
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#     def pop(self) -> int:
#         return self.queue1.popleft()
#
#     def top(self) -> int:
#         return self.queue1[0]
#
#     def empty(self) -> bool:
#         return not self.queue1

# 一个队列的解法
class MyStack:
    def __init__(self):
        self.queue = collections.deque()
    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return not self.queue

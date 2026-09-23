from dataclasses import dataclass, field
from typing import List, TypeVar

T = TypeVar("T")


# Stack
@dataclass
class Stack:
    items: List[T] = field(default_factory=list)

    def push(self, item: T):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# Queue
@dataclass
class Queue:
    items: List[T] = field(default_factory=list)

    def enqueue(self, item: T):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


# Test Stack
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.items)
print("Popped:", s.pop())


# Test Queue
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q.items)
print("Dequeued:", q.dequeue())
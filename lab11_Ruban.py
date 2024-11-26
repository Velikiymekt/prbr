#Task1
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        val = super().pop()
        self.__count += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

#Task2
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, element):
        self.__queue.insert(0, element)

    def get(self):
        if not self.__queue:
            raise QueueError("Черга порожня!")
        return self.__queue.pop()

try:
    q = Queue()
    q.put(1)
    q.put("dog")
    q.put(False)

    print(q.get())
    print(q.get())
    print(q.get())

    print(q.get())
except QueueError as e:
    print(f"Помилка: {e}")

#Task3
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, element):
        self.__queue.insert(0, element)

    def get(self):
        if not self.__queue:
            raise QueueError("Черга порожня!")
        return self.__queue.pop()

    def isempty(self):
        return len(self.__queue) == 0

class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Черга порожня")
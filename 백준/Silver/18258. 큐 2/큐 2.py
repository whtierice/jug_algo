

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,data):
        new_node = Node(data)
    
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.size +=1

        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size +=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            if self.front is self.rear:
                re = self.front.data
                self.front = None
                self.rear = None
                self.size-=1
                return re
            else:
                re = self.front.data
                self.front = self.front.next
                self.size-=1
                return re
        
    def floor(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            re = self.rear.data
            return re
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            re = self.front.data
            return re
    
    def is_empty(self):

        return self.front is None

    
    def get_size(self):
        return self.size
    

import sys

reps = int(sys.stdin.readline().strip())


# 큐 생성
q = Queue()

for i in range(reps):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == 'push':
        q.enqueue(command[1])
    elif command[0] == 'pop':
        if q.is_empty():
            print(-1)
        else:
            print(q.dequeue())
    elif command[0] == 'size':
        print(q.get_size())
    elif command[0] == 'empty':
        if q.is_empty():
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if q.is_empty():
            print(-1)
        else:
            print(q.peek())
    elif command[0] == 'back':
        if q.is_empty():
            print(-1)
        else:
            print(q.floor())          
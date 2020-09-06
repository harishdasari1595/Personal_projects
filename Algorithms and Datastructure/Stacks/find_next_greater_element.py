import sys

class node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def isempty(self):
        if self.top is None:
            return True
        return False
    
    def push (self,data):
        if self.isempty:
            self.top = node(data)
        else:
            new_node      = node(data)
            new_node.next = self.top
            self.top      = new_node
    def pop (self):
        if self.isempty:
            return "Cannot do more pop operation as stack is empty"
            sys.exit(0)
        value = self.top.data
        self.top = self.top.next
        return value

    def find_next_greater(self,arr):

        if len(arr) is None:
            return "array is empty please enter some value"
        self.push(arr[0])
        for i in range(1,n):
       
            if arr[i] < self.top.data:
                self.push(arr[i+1])
            if arr[i] > self.top.data:
                temp = arr[i]
                value = self.pop()
                while value < temp:
                    
                    value = self.pop()
                    print ("{} --> {}".format(value, temp))
                pus




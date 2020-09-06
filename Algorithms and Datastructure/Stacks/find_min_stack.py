import sys

class node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.first_min = None 
        self.curr_min  = None
        self.prev_min  = None

    def Is_empty(self):
        if self.top is None:
            return True
        return False

    def get_min(self):
        if self.top is  None:
            return "Stack is empty"
        else:
            print ("The minimum element in the stack is: {}".format(self.curr_min))
    

    def push(self,data):

        prev = self.prev_min
        curr = self.curr_min
        
        if self.top == None:
            self.top       = node(data)
            self.first_min = data
        elif data < self.first_min and prev == None:
            new_node = node(data)
            new_node.next = self.top
            self.curr_min = data
            self.prev_min = data
        elif data < self.curr_min:
            new_node = node(data)
            new_node.next = self.top
            curr = data
            self.prev_min = self.curr_min
            self.curr_min = curr
        else:
            new_node = node(data)
            new_node.next = self.top
            self.top = new_node
    def pop(self):

        if self.Is_empty():
            print("Stack Underflow")
            sys.exit(0)
        pop_value = self.top.data
        self.top = self.top.next
        if pop_value == self.curr_min:
            self.curr_min = self.prev_min
            if self.top.data < self.curr_min:
                self.curr_min = self.top.data
            elif self.top.next.data < self.curr_min:
                self.curr_min = self.top.next.data
            return pop_value
        elif pop_value > self.curr_min:
            return pop_value
        # elif self.top is None:
        #     self.curr_min = self.first_min
        #     return pop_value 
        else:
            return pop_value
if __name__=='__main__':
    stack=Stack()
    stack.push(10)
    stack.push(7)
    stack.push(6)
    stack.push(5)
    stack.get_min()
    ele=stack.pop()
    stack.get_min()
    print("poped Element in the stack is: {}" .format(ele))
    stack.push(-1)
    stack.get_min()






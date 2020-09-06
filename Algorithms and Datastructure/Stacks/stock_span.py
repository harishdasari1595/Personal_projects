import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class Stack: 

    def __init__(self): 
        self.top = None
        
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
    def push(self,data):
        self.temp=node(data)
        if self.temp is None:
            print("Stack overflow")
            return
        self.temp.next=self.top
        self.top=self.temp
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        self.top=self.top.next    
        return d
    
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        return d
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        self.p=self.top
        while self.p is not None:
            print(self.p.info)
            self.p=self.p.next

def calculateSpan(price,n,stock):
    # Instantiating the stack object
    s=Stack()
    # Pushing the first index value to the stack
    s.push(0)
    # Adding the first stock value in the stock list
    stock[0]=1
    
    for index in range(1,n):
        # Condition for poping the top of the stack if top < current index value
        while s.isEmpty() is not True and price[s.peek()]<=price[index]:
            ele=s.pop()
        # If stack is empty then cuurent stock index value is incremented by one
        if s.isEmpty():
            stock[index] = index + 1
        else:
            # Formula for calculating the span of the stock
            stock[index] = index - s.peek()
        # Pushing the index value of the current index value of the price list
        s.push(index)
    return stock


if __name__=='__main__':
    price=[100, 80, 60, 70, 60, 75, 85]
    n=len(price)
    stock=[0]*n
    stock=calculateSpan(price,n,stock)
    for i in stock:
        print("{} ".format(i)),










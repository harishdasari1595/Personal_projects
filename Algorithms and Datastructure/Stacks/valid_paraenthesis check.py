class node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__ (self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):

        self.temp = node(data)
        if self.temp is None:
            print  ("stackoverflow")
            return 
        self.temp.next = self.top
        self.top       = self.temp

    def pop(self):

        if self.top is None:
            print ("stack underflow")
            sys.exit(0)
        value    = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.isEmpty:
            print ("stack is empty")
            sys.exit(0)
        value = self.top.data
        return value


def balance_parenthesis_check(a, b):

    if(a==']' and b=='['):
        return 1
    if(a=='}' and b=='{'):
        return 1
    if(a==')' and b=='('):
        return 1
    return 0





def valid_parenthesis(expr):

    s = Stack()

    for i in range(len(expr)):
        
        if expr[i]== "{" or expr[i]== "[" or expr[i]== "(":
            s.push(expr[i])
            print ("element pushed {}".format(expr[i]))
        
        if expr[i]== "}" or expr[i]== "]" or expr[i]== ")":
            if s.isEmpty() is True:
                print ("Left parenthesis is more than right")
                return 0           
            else:
                value = s.pop()
                if balance_parenthesis_check(expr[i], value) !=1:
                    print ("Mismatch paraenthesis and expression is not balanced")
                    return 0
    
    
    if s.isEmpty is True:
        print ("The expression is balanced")
        return 1
    else:
        print ("There are more right parenthesis than left")
        return 0

if __name__=='__main__':
    s="((a+b)+(c+d))"
    valid=valid_parenthesis(s)
    if valid==1:
        print("Valid Expression")
    else:
        print("Invalid Expression")


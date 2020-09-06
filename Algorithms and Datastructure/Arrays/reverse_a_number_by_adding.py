
class node:
    def __init__(self,x):
        self.info = x
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_nodes_at_tail(self,data):
        temp = node(data)
        if not self.head:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp
        return self.head

    def display_nodes(self, head):

        if head is None:
            return head
        temp = head
        while temp:
            print (temp.info, end=" ")
            temp = temp.next
        
    
    def insert_nodes_at_head(self, value):
        temp = node(value)
        
        if self.head is None:
            self.head = temp
        temp.next = self.head
        self.head = temp
        return self.head 


    def reverse_llist(self, head):

        print("\n ################")
        self.display_nodes(head)
        
        prev    = None
        current = head
        Next    = current
        #Condition for checking the null condition
        while head is None:
            return
        
        #Loop for reversing the linked list
        while current is not None:
            Next         = current.next
            current.next = prev
            prev         = current
            current      = Next
        return prev


    def addTwoLists(self,first, second): 
        prev = None
        temp = None
        carry = 0 
        while(first is not None or second is not None): 

            fdata = 0 if first is None else first.info 
            sdata = 0 if second is None else second.info 
            Sum = carry + fdata + sdata 

            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum % 10

            temp = node(Sum) 

            if self.head is None: 
                self.head = temp 
            else : 
                prev.next = temp  

            prev = temp 
            if first is not None: 
                first = first.next
            if second is not None: 
                second = second.next

        if carry > 0: 
            temp.next = node(carry)  

if __name__ == "__main__":

    llist_1 = Linkedlist()
    llist_2 = Linkedlist()
    llist_3 = Linkedlist()
    a = [2,5,4]
    b = [4,5,8]
    first  = None
    second = None

    for i, values in enumerate(a):
        first = llist_1.insert_nodes_at_tail(values)
    
    for i, values in enumerate(b):
        second = llist_2.insert_nodes_at_tail(values)
    
    first     = llist_1.reverse_llist(first)
    second    = llist_2.reverse_llist(second)

    llist_3.addTwoLists(first, second)
    llist_3.display_nodes(llist_3.head)
    

    
    

                 

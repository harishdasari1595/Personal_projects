import sys

#Class for creating a node of a linked list  
class node:

    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:

    def __init__(self):
        #At start the head is pointing to None
        self.head = None

    def display(self):
        print ("#"*50)
        temp = self.head
        #print (msg)
        while (temp):
            print(temp.info)
            temp = temp.next

    #Method for inserting new node at the beginning
    def insert_at_beginning(self, i, data):
        #Creating the new node temp
        self.temp = node(data)
        #Check for a empty linked list
        if self.head is None:
            self.head = self.temp
            return
        #Pointing the next of the new node to the head node
        self.temp.next = self.head
        #Pointing the head to the new inserted node
        self.head      = self.temp
    
    def make_cycle(self, head, k):

        first_pointer  = head
        second_pointer = head

        for i in range(k):
            first_pointer = first_pointer.next
        
        while first_pointer is not None:
            first_pointer  = first_pointer.next
            second_pointer = second_pointer.next
        
        first_pointer.next = second_pointer
        return head

    def has_cycle(self, head):
        #Initializing the pointers and pointing to the head
        fast_pointer = head
        slow_pointer = head
        #Check for empty linked list
        if head is None:
            return False
        #Loop for detecting the cycle in the linked list
        while (slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if (slow_pointer == fast_pointer):
                return True
            
        return False

if __name__ == '__main__':

    llist = LinkedList()
    n = int(input("How many nodes do you want in the linked list: "))
    for i in range(n):
        llist.insert_at_beginning(i , int(input("Please enter the {} element ".format(i))))
    
    llist.display()
    cycle_list = llist.make_cycle(llist.head, 3)
    Result =  llist.has_cycle(cycle_list)
    print (Result)    



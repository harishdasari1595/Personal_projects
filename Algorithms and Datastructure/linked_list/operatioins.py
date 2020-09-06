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
    def insert_at_beginning(self, data):
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

    def insert_at_the_end(self, data):
        #Creating a new node to be inserted
        self.endtemp = node(data)
        #Checking for the empty list
        if self.head is None:
            self.head = self.endtemp
            return
        self.p = self.head
        while self.p.next:
            self.p = self.p.next

        self.p.next = self.endtemp
    
    def insert_at_given_node(self, data, target_node):
        #Creating the new node
        self.random_node = node(data)
        #Checking for the empty list
        if self.head is None:
            return "Match not found"

        self.p = self.head
        while self.p is not None:
            if (self.p.info == target_node):
                print ("match_found")
                self.random_node.next = self.p.next
                self.p.next = self.random_node
            
            self.p = self.p.next
        print ("Match not found")
    
    def delete_the_start_node(self, target_data):

        if self.head is None:
            print ("the node is empty")
            return
        if self.head.info == target_data:
            self.temp = self.head
            self.head = self.temp.next
            return 
        print ("This is not the first node please enter the first node")

    def swap_kth_node_fromend(self, n, k):
        #Creating a dummy node for handling the boundary case
        dummynode      = node(0)
        dummynode.next = self.head
        #Creating the required pointer and pointing to dummy node
        first_pointer  = dummynode
        second_pointer = dummynode
        temp_pointer   = dummynode
        
        if ((1 <= n <= 10^5) and (1 <= k < n)):
            
            if self.head is None:
                return "String is empty"

            for i in range (k):
                first_pointer = first_pointer.next
            
            while first_pointer is not None:
                first_pointer  = first_pointer.next
                second_pointer = second_pointer.next
                temp_pointer   = temp_pointer.next
                
            temp_pointer.info        = second_pointer.info 
            second_pointer.info      = second_pointer.next.info
            second_pointer.next.info = temp_pointer.info
            return dummynode.next
            


            
        
if __name__ == '__main__':

    llist = LinkedList()
    n = int(input("How many nodes do you want in the linked list: "))
    for i in range(n):
        llist.insert_at_beginning(int(input("Please enter the {} element ".format(i))))

    llist.display()
    llist.swap_kth_node_fromend(n, 2)
    llist.display()
    #print (llist.head.info)

    
    # llist.insert_at_the_end(int(input("What do you want to insert at the end ")))
    # llist.display()

    # llist.insert_at_given_node(int(input("What is the value you want to insert ")), int(input("After which node you want to insert ")))
    # llist.display()

    # llist.delete_the_start_node(int(input("Which node you want to delete ")))
    # llist.display()


   
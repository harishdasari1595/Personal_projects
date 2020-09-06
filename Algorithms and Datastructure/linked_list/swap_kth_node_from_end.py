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

    def swap_kth_node_fromend(self, n, k):
        #Creating a dummy node for handling the boundary case
        dummynode      = node(0)
        dummynode.next = self.head
        #Creating the required pointer and pointing to dummy node
        first_pointer  = self.head
        second_pointer = self.head
        temp_pointer   = self.head
        
        if ((1 <= n <= 10^5) and (1 <= k < n)):
            
            if self.head is None:
                return "String is empty"

            for i in range (k):
                first_pointer = first_pointer.next
            
            while first_pointer is not None:
                first_pointer  = first_pointer.next
                second_pointer = second_pointer.next
                temp_pointer   = temp_pointer.next

            # print ("first pointer value is {} ".format(first_pointer))
            # print ("second pointer value is {} ".format(second_pointer.info))
            # print ("Temp pointer value is {} ".format(temp_pointer.info))    
            # print ("*"*50)
            temp                = second_pointer.info 
            knext_value         = second_pointer.next.info
            second_pointer.info = knext_value
            second_pointer.next.info = temp
            return dummynode.next
            


            
        
if __name__ == '__main__':

    llist = LinkedList()
    n = int(input("How many nodes do you want in the linked list: "))
    for i in range(n):
        llist.insert_at_beginning(int(input("Please enter the {} element ".format(i))))

    llist.display()
    llist.swap_kth_node_fromend(n, 3)
    llist.display()








# Class for creating the node of the linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for creating the linkedlist and its functionality
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Method for inserting the nodes into the linkedlist
    def insert_node(self, data):
        # Creating the data node
        temp = Node(data)
        # Initial check if the llist is empty
        if self.head is None:
            # Inserting the first node at the head
           self.head = temp

        else:
            # Inserting at the tail end of the linkedlist
            self.tail.next = temp
        self.tail = temp

    # Method for displaying the linkedlist
    def display_llist(self, head):
        while head != None:
            print (head.data, end = " ")
            head = head.next
    
    # Method for converting the llist starting from odd numbered node followed by the even nodes
    def odd_even(self, head):
        # Boundary cases where there are No node, single node and double node in the linked-list 
        if not head or not head.next or not head.next.next:
            return head
        # Creating odd and even pointers for traversing the llist
        odd   = head
        even  = head.next
        # Creating pointer for tracking the even list head
        even_head = even
        # Main loop for traversing and performing the whole logic
        while even and even.next:
            # Finding the next odd node
            odd.next = even.next
            odd = odd.next 
            # Finding the next even node
            even.next = odd.next
            even      = even.next
        # Attaching the even head after arranging the whole odd node llist
        odd.next = even_head
        return head

if __name__ ==  "__main__":
    
    # Creating the linkedlist object 
    llist = Linkedlist()
    # Taking the input for the number of nodes
    Number_of_nodes = int(input())
    # Taking the node value from the user
    for index in range(Number_of_nodes):
        llist.insert_node(int(input()))
    # Displaying the initial linkedlist
    llist.display_llist(llist.head)
    # Arranging the odd and even linkedlist
    head = llist.odd_even(llist.head)
    # Displaying the linkedlist after arranging the odd and even terms
    print ("\n")
    llist.display_llist(head)

    



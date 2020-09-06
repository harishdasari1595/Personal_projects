
class node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedLiist:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):

        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp

    def display_llist(self, head):

        while head != None:
            print (head.data, end = " ")
            head = head.next
   

    def make_alternate_nodes(self, head):

        currNode = head
        if (currNode is None or currNode.next == None):
            return

        self.head1 = currNode
        self.head2 = currNode.next 

        while (currNode != None and currNode.next != None):
            # Creating temporary pointer for traversing the original llist
            temp = currNode.next
            # Creating the next node value of list A
            currNode.next = temp.next
            # Check for the availability of the next node for the listB
            if (currNode.next != None and currNode.next.next != None):
                # Adding the next value of list B
                temp.next = currNode.next.next
            else:
                # Indicating the end of the llist
                temp.next = None
                return
            # Keep moving the temporary pointer
            currNode = currNode.next    
        
llist = LinkedLiist()
n     = int (input("How many nodes do you want in the linked_list: "))

for i in range(n):
    llist.insert_node(int(input("Please enter the {} element: ".format(i))))

llist.make_alternate_nodes(llist.head)

llist.display_llist(llist.head1)

llist.display_llist(llist.head2)
    

        
            
           


class node():
    def __init__(self, x):

        self.data = x
        self.next = None

class Linked_list():

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
    
    def display_linked_list(self, head):

        if head is None:
            return
        while head is not None:
            print (head.data , end= " ")
            head = head.next
    
    def reverse(self, head, new_head):

        if head is None:
            return new_head
        Next      = head.next
        head.next = new_head
        new_head  = head
        head      = Next
        return self.reverse(head, new_head)
    
    def reverse_linkedllist(self, head):

        return self.reverse(head, None)

llist = Linked_list()

number_of_nodes = int(input("How many nodes do you want in the linked list: "))

for i in range (number_of_nodes):
    llist.insert_node(int(input("Please enter the {} node: ".format(i))))
#llist.display_linked_list(llist.head)
new_head = llist.reverse_linkedllist(llist.head)
llist.display_linked_list(new_head)

    

    
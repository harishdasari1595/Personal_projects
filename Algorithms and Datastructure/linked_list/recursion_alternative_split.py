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
    
    def arrange_nodes(self, head1, head2):
        
        if (head1 == None or head2 == None):
            return
        if (head1 != None and head2.next != None):
            #Creating the next node value of list A
            head1.next = head1.next.next
        #Check for the availability of the next node for the listB
        if (head1.next != None and head2.next.next != None):
            #Adding the next value of list B
            head2.next = head2.next.next
        self.arrange_nodes(head1, head2)   
   

    def alternatesplit_llist(self, head):

        currNode = head
        
        self.head1 = currNode
        self.head2 = currNode.next 
        
        First_head  = self.head1
        second_head = self.head2 
        
        self.arrange_nodes(First_head, second_head)
        return (head)

       
    
if __name__ == "__main__":
    
    llist = LinkedLiist()
    number_of_nodes = int(input())
    if 1 <= number_of_nodes <= 10**5:
        for i, value in enumerate(input().split()):
            print (value)
            llist.insert_node(value)
        
        llist.alternatesplit_llist(llist.head)
        llist.display_llist(llist.head1)
        print("\nb")
        llist.display_llist(llist.head2)
    
    
    
    
    
    
    

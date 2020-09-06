#Class for creating the node of the linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Class for creating the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def display_linked_list(self, head):
        while head:
            print (head.data, end = " ")
            head = head.next
            
    def insert_node(self,data):
        temp = node(data)
        if not self.head:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp
                
    def reverse_linked_list(self, head):
        prev    = None
        current = head
        if head is None:
            return "NO"
        while current is not None:
            future       = current.next
            current.next = prev
            prev         = current
            current      = future
        head = prev
        return head
    
    def find_middle_node(self, head):
        
        fast_pointer = head
        slow_pointer = head
        if head is None:
            return head
        while (fast_pointer.next is not None) and (fast_pointer.next.next is not None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return slow_pointer
    
    def compare_list_nodes(self, head1,head2):
        while head1 != None and head2 != None:
            if head1.data == head2.data:
                #print (head1.data, head2.data)
                head1 = head1.next
                head2 = head2.next
            else:
                return "NO"
        return "YES"
            
    def is_pallindrome(self, head):
        
       
        if self.head is None:
            return "NO"
        slow_pointer      = self.find_middle_node(head)
        second_list       = slow_pointer.next 
        slow_pointer.next = None
        second_head       = self.reverse_linked_list(second_list) 
        result            = self.compare_list_nodes(head, second_head)
        return result

        
if __name__ == "__main__":
    
    #Initializing the linked list object
    llist = LinkedList()
    
    #Taking input as the lenght of the string
    n = int(input())
    if (1 <= n <= 10**5):
        for i,value in enumerate(input()):
            llist.insert_node(value)
        RESULT = llist.is_pallindrome(llist.head)
        print (RESULT)
         
    else:
        print ("NO")
        

        
        
        
        
        
        
    
        
        
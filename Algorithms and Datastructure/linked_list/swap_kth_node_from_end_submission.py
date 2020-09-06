#Class for creating a node of a linked list  
class node:

    def __init__(self, info):
        self.info = info
        self.next = None

#Class for creating complete linked list
class LinkedList:

    def __init__(self):
        #At start the head is pointing to None
        self.head = None
    
    #Method for formatting the output
    def output_formatter(self, output_list):
        output_string = ""
        return ' '.join(map(str, output_list)) 
    
    #Method for displaying the swapped output linked list    
    def display_linked_list(self):
        temp = self.head
        output_list = []
        while (temp):
            #print(temp.info)
            output_list.append(str(temp.info))
            temp = temp.next
        print(self.output_formatter(output_list))
        output_list.clear()
       
    #Method for inserting new node at the end
    def insert_the_node(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.p = self.head
        while self.p.next is not None:
            self.p=self.p.next
        self.p.next = self.temp;
    
    #Method for swapping the kth node fromend
    def swap_kth_node_fromend(self, n, k):
       
        #Creating the required pointer and pointing to dummy node
        first_pointer  = self.head
        second_pointer = self.head
        if ((1 <= n <= 10^5) and (1 <= k < n)):
            if self.head is None:
                return False
            for i in range (k):
                first_pointer = first_pointer.next
            while first_pointer is not None:
                first_pointer  = first_pointer.next
                second_pointer = second_pointer.next
            #Swapping the kth and k-i th node
            temp                     = second_pointer.info 
            knext_value              = second_pointer.next.info
            second_pointer.info      = knext_value
            second_pointer.next.info = temp
        return False
            
        
if __name__ == '__main__':

    #Initializing the linked list object
    llist = LinkedList()
    #Taking the length and kth position for swapping
    Input_string = input()
   
    #Taking the input for inserting into the linked list
    #Inserting the data values into the linked list
    for i, value in enumerate(input().split()):
        llist.insert_the_node(value)

    llist.swap_kth_node_fromend(int(Input_string[0]),int(Input_string[2]))
    llist.display_linked_list()


class Node:   
    def __init__(self,value):
        self.next = None
        self.val = value
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data): 
        if self.head is None:
            self.head = Node(data)
            return
        
        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = Node(data)
                
    def listPrint(self):
        cur = self.head
        while (cur):
            print(cur.val)
            cur = cur.next
            
    def listReverse(self):
        cur = self.head
        prev = None
        while (cur != None):
            nextl = cur.next
            cur.next = prev
            prev = cur
            cur = nextl 
        self.head = prev
        

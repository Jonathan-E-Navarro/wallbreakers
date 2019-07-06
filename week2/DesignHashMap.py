class ListNode:
    #simple listnode class for our linked lists
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        #initalize size of the hashtable to a large number to avoid collisions 
        self.size = 10000 
        #intialize table to size 
        self.table = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        bucket = key % self.size
        current = self.table[bucket]
        #if linked list exists 
        if current:
            while True:
                if current.key == key:
                    current.val= value
                    return
                elif current.next == None:
                    current.next = ListNode(key,value)
                    break
                else:
                    current = current.next
            
        else:
            #create linked list
            self.table[bucket] = ListNode(key,value)

            
    def get(self, key: int) -> int:
        bucket = key % self.size
        current = self.table[bucket]
        #if linked list exists
        if current:
            while current:
                if current.key == key:
                    return current.val
                else:
                    current = current.next
                    
        #linked lists and therefore objects does not exist in this bucket
        return -1

        

    def remove(self, key: int) -> None:
        bucket = key % self.size
        current = self.table[bucket]
        #If bucket 
        if current:
            prev = ListNode(None,None)
            prev.next = current
            ans = prev
            while current:
                if current.key == key:
                    prev.next = current.next
                    self.table[bucket] = ans.next
                    break
                else:
                    prev, current = current, current.next
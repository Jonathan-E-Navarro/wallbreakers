class ListNode:
    #simple listnode class for our linked lists
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #initalize size of the hashtable to a large number to avoid collisions 
        self.size = 10000 
        #intialize table to size 
        self.table = [None] * self.size
    

    def add(self, key: int) -> None:
        bucket = key % self.size
        current = self.table[bucket]
        
        #if linked list exists 
        if current:
            while True:
                if current.key == key:
                    return
                elif current.next == None:
                    current.next = ListNode(key)
                    break
                else:
                    current = current.next
            
        else:
            #create linked list
            self.table[bucket] = ListNode(key)
        

    def remove(self, key: int) -> None:
        bucket = key % self.size
        current = self.table[bucket]
        #If bucket 
        if current:
            prev = ListNode(None)
            prev.next = current
            ans = prev
            while current:
                if current.key == key:
                    prev.next = current.next
                    self.table[bucket] = ans.next
                    break
                else:
                    prev, current = current, current.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = key % self.size
        current = self.table[bucket]
        #if linked list exists 
        if current:
            while True:
                if current.key == key:
                    return True
                elif current.next == None:
                    return False
                else:
                    current = current.next
            
        else:
            #linked list does not exist
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
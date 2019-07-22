'''
Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.
When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
'''
from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict() 
        self.remain = capacity

    def get(self, key):
        #if value not in cache
        if key not in self.dic:
            return -1
        #pop off value that we are going to return
        v = self.dic.pop(key) 
        # set same key as the value,so itll be newest value in dict
        self.dic[key] = v   
        return v
        

    def put(self, key, value):
        #if key already in dict, pop it off
        if key in self.dic:    
            self.dic.pop(key)
        else:
            #if not full, update fill status
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full, pop off LRU item
                self.dic.popitem(last=False) 
        #set new key to value 
        self.dic[key] = value
        
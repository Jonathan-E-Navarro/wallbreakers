class MyStack:
    '''
    queue: first in first out | push to back (append), peek,pop from front (pop(0)), size, is empty
    [1,2,3,4]
    pop from front  = > [2,3,4]  
    push 5 to back => [2,3,4,5]  
    
    
    stack: last in first out   
    [1,2,3,4]
    pop from top => [1,2,3]
    push 5 to stack => [1,2,3,5]
    
    simulate stack with queue:
    to pop off stack we use two queues 
    pop from front of our queue and add to new queue until we get
    to the last one
    
    
    
    to push on to stack 
    to pop off the stack 
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.top_element = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.top_element = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop(0))

        ans = self.queue.pop()
        self.queue = temp
        self.top_element = self.queue[-1] if len(self.queue) > 0 else None
        return ans
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_element
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
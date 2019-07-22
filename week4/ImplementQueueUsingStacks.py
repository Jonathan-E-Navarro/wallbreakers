class MyQueue:
    '''
    queue: first in first out | push to back (append), peek,pop from front (pop(0)), size, is empty
    [1,2,3,4]
    pop from front  = > [2,3,4]  
    push 5 to back => [2,3,4,5]  
    
    
    stack: last in first out   
    [1,2,3,4]
    pop from top => [1,2,3]
    push 5 to stack => [1,2,3,5]
    
    how simulate stack with queue:  pop(),peek[-1],push onto stack, append
    stack1 = []
    stack2 = []
    
    to push on to stack 
    [1,2]
    to pop off the stack 
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # print('pushing!')
        self.stack.append(x)
        # print(self.stack)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # print("popping from front!")
        if len(self.stack) == 0:
            return
        temp = []
        while len(self.stack) > 1:
            temp = [self.stack.pop()]+temp
            # print("temp: ",temp)
            
        ans = self.stack.pop()
        # print("front element: ",ans)
        self.stack = temp
        return ans
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        # print("peeking!")
        if len(self.stack) == 0:
            return
        temp = self.stack[:]
        # print("temp: ",temp)
        while len(temp) > 1:
            temp.pop()
            
        ans = temp.pop()
        # print("front element is: ",ans)
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # print("")
        if len(self.stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
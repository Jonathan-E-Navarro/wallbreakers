class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            # temp = s[i]
            # s[i] = s[len(s)-1-i]
            # s[len(s)-1-i] = temp
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]           

"""
Thought process:
We need to reverse the string in place 
for example hello -> olleh 

what we can do is iterate up to len(str)//2 -> our midpoint 
and swap our outermost left index and our outermost right index. 
This is basically using the two pointer method 

For example:
hello -> oellh ->olelh -> olleh ! :]
"""
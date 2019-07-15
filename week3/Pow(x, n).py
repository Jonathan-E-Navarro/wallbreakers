class Solution:
    '''
    2.1 ^ 3 
    (2.1, 3) => (2.1, 2) => (2.1, 1)
             <=   4.41   <=     2.1
             
    how to eliminate recursive calls, pair together groups of two, :
    what ends up happening is x gets squared and n gets halved 
    2^8 = 2*2*2*2*2*2*2*2 = 256 
    4^4 = 4*4*4*4
    16^2 = 16*16
    
    
    3^8 = 3*3*3*3*3*3*3*3 = 6561
    9^4 = 9*9*9*9 = 6561
    81^2 = 81*81 = 6561
    
    odd instances:  (squared(x) ^ (n-1/2)* remaining x 
    3^7 = 3*3*3*3*3*3*3 = 2187
        9 * 9 * 9 * 3 = (9^3)*3 
            81  * 9  = ((81^1)*9)*3 = 2187 
    '''
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            #invert x and produce a positive n 
            return self.myPow(1/x,abs(n))  
        elif(n%2==0):
            return self.myPow(x*x,n/2);
        else:
            print(x*x,(n-1)/2,x)
            return self.myPow(x*x,(n-1)/2)*x;


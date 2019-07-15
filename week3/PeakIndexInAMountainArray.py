class Solution:
    def is_peak(self,array,index):
        #if first item
        if index == 0:
            if array[index+1] < array[index]:
                print("first is a peak")
                return True
        #if last item
        elif index == len(array)-1:
            if array[index-1] < array[index]:
                return True
        #if any item in between
        elif index in range(1,len(array)):
            if array[index-1] < array[index] and  array[index+1] < array[index]:
                return True
                
        return False
        
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0 
        prev = ''
        peak = ''
        
        for idx in range(len(A)):
            if self.is_peak(A,idx):
                if peak == '':
                    peak = idx 
                else:
                    if A[idx] > A[peak]:
                        peak = idx
        return peak


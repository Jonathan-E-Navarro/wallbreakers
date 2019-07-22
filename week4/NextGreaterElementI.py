class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        for num in nums1:
            if num in nums2:
                sublist = nums2[nums2.index(num)+1:]
                found = False
                
                for num2 in sublist:
                    if num2 > num:
                        results.append(num2)
                        found = True
                        break
                if not found:
                    results.append(-1)
                        
            else:
                results.append(-1)
        
        return results
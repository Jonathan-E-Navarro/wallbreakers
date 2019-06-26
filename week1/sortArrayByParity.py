class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for number in A:
            if number%2 == 0:
                list1.append(number)
            else:
                list2.append(number)
        return list1+list2
        
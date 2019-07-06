class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        # print(set1)
        # print(set2)
        return([item for item in set1.intersection(set2)])
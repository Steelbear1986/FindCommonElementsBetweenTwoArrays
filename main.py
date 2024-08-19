class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        return (
        [sum(val for i, val in nums1.items() if i in nums2), sum(val for i, val in nums2.items() if i in nums1)])

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         # Initialize the slow pointer
#         slow = 0
        
#         # Iterate through the array with the fast pointer
#         for fast in range(1, len(nums)):
#             if nums[fast] != nums[slow]:
#                 slow += 1
#                 nums[slow] = nums[fast]
        
#         # Return the length of the unique elements
#         return slow + 1
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    
        # Initialize the first pointer
        i = 0
    
        # Start iterating from the second element
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
    
        # The number of unique elements is i + 1
        return i + 1

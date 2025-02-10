# MEDIUM
# 128. Longest Consecutive Sequence
# Medium
# Topics
# Companies

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        # convert your intiial array to a set
        
        set_arr = set(nums)
        longest = 0
        
        for num in nums:
            #check if it's the start of a sequence
            if(num - 1) not in set_arr:
                length = 0
                while(num + length) in set_arr:
                    length +=1
                longest = max(length, longest)
            return longest
        
        #start of a sequence will not have a left neighbor
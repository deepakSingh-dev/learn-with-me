# 128. Longest Consecutive Sequence

# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
 
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0

        for n in num_set:
            # 1. ONLY start if 'n' is the absolute beginning of a sequence
            if n - 1 not in num_set:
                current_number = n
                current_sequence = 1

                # 2. Use 'current_number' to move forward, not 'n'
                while current_number + 1 in num_set:
                    current_number += 1  # Updates the pointer so the loop terminates
                    current_sequence += 1 # Increments the local streak tracker

                # 3. Update the global maximum only after the sequence ends
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
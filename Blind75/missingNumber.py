class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i, val in enumerate(nums):
          xor ^= i ^ val
        return xor ^ len(nums)   # XOR in the last index n
        
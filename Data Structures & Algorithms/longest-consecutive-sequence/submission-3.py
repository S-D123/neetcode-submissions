class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(list(nums))
        maxLen = 0 # for final answer and comparing purposes

        lenth = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                lenth += 1
            else:
                maxLen = max(maxLen, lenth)
                lenth = 1

        if maxLen > len(nums) or lenth > len(nums): return 0

        return max(maxLen, lenth)
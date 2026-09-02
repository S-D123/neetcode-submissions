class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)

        d = dict()
        for num in nums:
            if num not in d: d[num] = 1
            else: d[num] += 1

        ans = []
        for i in range(k):
            high = 0
            num = 0

            for key, values in d.items():
                if values > high: 
                    high = values
                    num = key

            d[num] = 0
            ans.append(num)

        return ans
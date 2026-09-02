class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucket sort

        buckets = [[] for _ in range(1, len(nums)+1)] 
        # each index is a => frequency 
        d = dict() # contains => number : frequency
        
        # calc frequency
        for num in nums: d[num] = d.get(num, -1) + 1

        # add in the buckets
        for key, value in d.items(): buckets[value].append(key)

        # for answer
        ans = []
        for i in range(len(buckets)-1, -1, -1):
            if k <= 0: return ans
            if buckets[i]:
                ans += buckets[i]
                k -= len(buckets[i])
        return ans
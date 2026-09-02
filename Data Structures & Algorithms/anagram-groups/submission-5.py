from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedStr = []
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            sortedStr.append(word)

        d = defaultdict(list)
        for i in range(len(sortedStr)):
            word = sortedStr[i]
            d[word].append(strs[i])

        return list(d.values())
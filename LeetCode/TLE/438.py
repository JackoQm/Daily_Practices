'''
    From: LeetCode - 438. Find All Anagrams in a String
    Level: Easy
    Source: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
    Status: TLE
	Solution: Using Brute Force
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        dicts = {c: p.count(c) for c in p}
        end = len(s) - len(p) + 1
        result = []
        i = 0
        while i < end:
            dic = dicts.copy()
            for j in range(i, i+len(p)):
                if s[j] not in dic.keys():
                    dic[s[j]] = -1
                    i = j
                    break
                elif dic[s[j]] == 0:
                    dic[s[j]] = -1
                    break
                else:
                    dic[s[j]] -= 1
            # print(dic)
            if -1 not in dic.values():
                result.append(i)
            i += 1
        return result  

# times o(n^2)
# space o(n)

'''
Most Optimal Answer: Sliding window
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(p) > len(s):
            return result
        begin, end, length = 0, 0, len(s)
        dic = {c: p.count(c) for c in p}
        count = len(dic.keys())
        
        while end < length:
            c = s[end]
            if c in dic.keys():
                dic[c] -= 1
                if dic[c] == 0:
                    count -= 1
            end += 1
            while count == 0:
                ch = s[begin]
                if ch in dic:
                    dic[ch] += 1
                    if dic[ch] > 0:
                        count += 1
                if end - begin == len(p):
                    result.append(begin)
                begin += 1
        return result

# times o(n)
# space o(n)
'''
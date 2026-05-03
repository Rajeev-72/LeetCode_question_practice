from typing import List

"""
LeetCode 14: Longest Common Prefix

Approach:
- Start with first string as prefix
- Compare with each string
- Reduce prefix until match

Time Complexity: O(n * m)
Space Complexity: O(1)
"""




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            i = 0
            while i < min(len(prefix), len(word)) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]

        return prefix
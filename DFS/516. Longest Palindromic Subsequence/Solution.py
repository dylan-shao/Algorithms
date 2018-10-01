# See another solution in DP
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = len(s) - 1
        return self.__dfs(s, i, j, {})

    def __dfs(self, s, start, end, dic):
        if start > end:
            return 0
        if start == end:
            return 1

        if (start,end) in dic:
            return dic[(start,end)]

        if s[start] == s[end]:
            res = self.__dfs(s, start + 1, end - 1,dic) + 2
            dic[(start,end)] = res
        else:
            res = max(self.__dfs(s, start + 1, end,dic),self.__dfs(s, start, end - 1,dic))
            dic[(start,end)] = res
        return res

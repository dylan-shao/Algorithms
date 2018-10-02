class Solution:
    # time O(n^2)
    # space O(n^2)
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = len(s) - 1
        dp = [[0]*len(s) for _ in range(len(s))]
        res = 0 if len(s) == 0 else 1
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    res = max(res, dp[i][j])
        return res

    # time O(n^2)
    # O(n) space
    def longestPalindromeSubseq2(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = len(s) - 1
        dp = [0]*len(s)
        res = 0 if len(s) == 0 else 1
        for i in range(len(s)-1, -1, -1):
            dp[i] = 1
            extra1 = 0
            for j in range(i+1, len(s)):
                extra2 = 0
                if s[i] == s[j]:
                    extra2 = extra1 + 2
                    res = max(res, extra2)
                else:
                    extra2 = max(dp[j-1], dp[j])
                    res = max(res, extra2)
                extra1 = dp[j]
                dp[j] = extra2


        return res


#-------------------------- DFS --------------------------------------
# time O(2^n)
# pace O(n)
class Solution2:
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

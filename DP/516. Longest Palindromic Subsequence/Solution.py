class Solution:
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

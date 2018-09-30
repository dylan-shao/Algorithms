class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                    res = max(dp[i], res)

                if s[i-1] == ')' and dp[i-1] > 0:
                    # start index for i,
                    # i - dp[i-1] - 1 ----> '(' ( () ) ')' --> i
                    startIndex = i - dp[i-1] - 1
                    if startIndex >=0 and s[startIndex] == '(':
                        dp[i] = dp[i-1] + dp[startIndex-1] + 2
                        res = max(dp[i], res)
        return res

        

# dp
# time O(m*n):
# space O(m*n)
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1)+1
        n = len(s2)+1
        dp = [[False]*(n) for _ in range(m)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]

        return dp[len(s1)][len(s2)]

#-------------- DFS ----------------------
# time O(2^(m+n))
# space O(m+n)
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) < len(s3):
            return False

        return self.__dfs(s1,s2,s3)

    def __dfs(self, s1,s2,s3):
        if len(s3) == 0:
            return len(s1) == 0 and len(s2) == 0
        if len(s3) == 1:
            return s3 == s1 + s2 or s3 == s2 + s1

        substr1 = len(s1) > 0 and s1[-1] == s3[-1] and self.__dfs(s1[:-1],s2, s3[:-1])
        substr2 = len(s2) > 0 and s2[-1] == s3[-1] and self.__dfs(s1,s2[:-1], s3[:-1])
        return substr1 or substr2

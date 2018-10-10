### summary

#### compare dp with the dfs:
```python
dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]

substr1 = len(s1) > 0 and s1[-1] == s3[-1] and self.__dfs(s1[:-1],s2, s3[:-1])
substr2 = len(s2) > 0 and s2[-1] == s3[-1] and self.__dfs(s1,s2[:-1], s3[:-1])
```
dfs calls from top to bottom, and execute from bottom
dp is executed from "bottom"(beginning) to end
so reverse `s1[-1] == s3[-1] and self.__dfs(s1[:-1],s2, s3[:-1])`
we got `s1[i-1] == s3[i+j-1] and dp[i-1][j]`

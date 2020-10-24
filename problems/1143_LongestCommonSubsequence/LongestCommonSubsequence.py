class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)

        # 注意，这里申请的数组在行和列方向上均扩充了一维
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # 注意：在申请二维数组的时候一定要搞清楚谁做行谁做列，
        # 否则在运行代码的时候就会出现索引越界的错误。
        # 比如说这里，一定是内部 in range(n+1)，外部 in range(m+1)，
        # 而不是内部 in range(m+1)，外部 in range(n+1)。

        # 注意：这里两层循环均从1开始
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:     # 这里边索引的细节非常多，
                    dp[i][j] = dp[i-1][j-1] + 1  # 一定要注意
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
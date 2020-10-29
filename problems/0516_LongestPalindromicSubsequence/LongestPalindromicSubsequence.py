# 注：实际写代码时不需要import numpy，这里只是为了debug用的
import numpy as np


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for i in range(n)]
        
        # 注：倒着遍历时，第一个数字是可以取到的，所以这里必须
        # 写n-1，不能写n
        for i in range(n-1, -1, -1):
            
            # 对角线位置必须特殊处理
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        # 这里的dp其实是一个上三角矩阵
        print(f'\ndp = \n{np.array(dp)}')
        
        return dp[0][-1]


if __name__ == '__main__':
    sol = Solution()
    s = "bbbab"
    res = sol.longestPalindromeSubseq(s)
    print(f'\nres = {res}')


"""Result:
dp =
[[1 2 3 3 4]
 [0 1 2 2 3]
 [0 0 1 1 3]
 [0 0 0 1 1]
 [0 0 0 0 1]]

res = 4
"""
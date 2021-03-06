class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n+1): # 注意这个地方的范围是(1, n+1)
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]= True
                    break
        
        return dp[-1]
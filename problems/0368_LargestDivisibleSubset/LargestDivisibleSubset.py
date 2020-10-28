class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # 这里必须要对edge case单独处理
        if n == 0:
            return []
        
        # 这里先进行排序可以省去很多麻烦
        nums.sort()
        
        # 申请一个dp数组
        # dp[i]表示截止到第i个位置处，最长LDS的长度
        # 这里和Longest Increasing Subsequence是比较像的
        dp = [1] * n # 默认到每一个位置时，LDS的长度都至少为1
        
        # parent数组用于保存回溯路径，方便返回最终结果
        parent = [0] * n # 默认每一个位置的LDS都从第0号元素开始
        
        # max_len用于记录所有LDS的最长长度
        # max_idx用于记录最长LDS的最后一个元素位置
        max_len, max_idx = 1, 0
        
        for i in range(n):
            for j in range(i-1, -1, -1): # 后面的回溯决定了这个地方必须用倒序
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        print(f'parent = {parent}')
        print(f'dp = {dp}')
        print(f'max_len = {max_len}')

        res = []
        # 之所以可以用这个for循环，是因为最长LDS的长度是max_len。
        # 也就是说我们只需要循环max_len轮就可以把所有需要的元素
        # 添加进去，而且既不会多也不会少。
        for i in range(max_len):
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
        
        return res[::-1]
                

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 8, 9, 12, 15, 45, 135]
    # nums = [1, 2, 3]
    # nums = [4, 8, 10, 240]
    # nums = [3, 4, 16, 8]
    res = sol.largestDivisibleSubset(nums)
    print(f'\nfinal_res = {res}')


"""Result:
parent = [0, 0, 0, 1, 0, 3, 2, 3, 4, 8, 9]
dp = [1, 2, 2, 3, 2, 4, 3, 4, 3, 4, 5]
max_len = 5

final_res = [1, 5, 15, 45, 135]
"""
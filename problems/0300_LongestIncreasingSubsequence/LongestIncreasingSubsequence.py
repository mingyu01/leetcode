"""
    O(n^2)的解法：
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # 这里需要申请一个全为1的dp数组，数组的长度和nums的长度相同
        # 为什么是全1：因为到每一个位置为止，最短的LIS的长度都是1（即
        # 这个数字本身）
        dp = [1 for i in range(n)]

        # 和word break 一样，包含两层循环
        for i in range(n):
            for k in range(i):
                # 注意这里dp数组的更新条件：不是每遍历到一个k位置都会
                # 进行更新，只有当nums[i]>nums[k]时才进行更新
                if nums[i] > nums[k]:
                    # 更新的时候必须取max，否则最大值可能被湮没掉
                    # 这道题中有两个需要取max的地方，这里是第一个，
                    # 另外一个是在返回的时候
                    dp[i] = max(dp[i], dp[k]+1)
        
        # 注意：dp[-1]不一定是整个dp数组中的最大值，因此在返回的时候，
        # 不能返回dp[-1]，而应该返回max(dp)
        return max(dp) if n != 0 else 0



"""
    O(nlogn)的解法：
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 首先要申请一个全0的tails数组，长度和nums的长度一样
        tails = [0 for i in range(len(nums))]

        # size表示tails数组的长度，初始时tails中没有有效元素，故
        # size置零
        size = 0
        
        # 遍历的时候直接去遍历nums中的数就可以，不需要遍历下标
        for num in nums:

            # 每次新来一个数，i都是从tails的头部重新开始进行二分查找
            # 而j，其实指向的并不是tails数组的尾部，而是尾部元素的下一个
            # 位置。这样当while循环退出的时候，i=j，如果我们想在tails的
            # 尾部插入一个元素，直接赋值给tails[i]就可以了（因为i=j，指向
            # 的恰好是原tails数组尾部的下一个位置。）
            i, j = 0, size

            # 二分查找
            while i != j:
                m = (i + j) // 2
                if num > tails[m]:
                    i = m + 1
                else:
                    j = m
            
            # 在最终的i位置上替换元素
            tails[i] = num

            # 动态取max
            # 这里为什么是i+1?原因是这样的：假设tails中只有一个元素，
            # 那么tails[0]=num，而此时tails中元素的长度其实是1，也就是说
            # 长度和i的索引相差了1（因为索引从0开始，而长度从1开始计数），
            # 因此这里要加上1进行补偿。
            size = max(size, i + 1)
        
        # 最终return size 即可。
        return size
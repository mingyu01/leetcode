class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        num_set = set(nums) # 注意：这里要进行去重
        
        for num in num_set:
            if num-1 not in num_set:
                y = num + 1
                while y in num_set:
                    y += 1
                length = max(length, y-num)
                # 注意：最终的长度是y-num，而不是y-num+1，因为
                # y在跳出循环时额外加上了1，y-num就等价于原来的
                # y-num+1了
        
        return length

if __name__ == '__main__':
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    res = sol.longestConsecutive(nums)
    print(f'res = {res}')



"""
输出结果：res = 4
"""
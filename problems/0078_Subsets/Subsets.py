class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [ele+[num] for ele in res]
            print(f'res = {res}')
        
        return res



if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    res = sol.subsets(nums)
    print(res)



"""Results:
res = [[], [1]]
res = [[], [1], [2], [1, 2]]
res = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
"""

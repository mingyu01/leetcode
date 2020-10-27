class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        cur_max = cur_min = final_max = nums[0]
        for i in range(1, len(nums)): # 注意这里索引必须从1开始

            # 这里nums[i]的参与，保证了序列一定是连续的（可以见下面的结果输出）
            candidates = (nums[i], cur_max*nums[i], cur_min*nums[i])
            # 为什么还要比较cur_min呢？这是由数的乘法的性质决定的：
            # 一个很大的数在乘以一个负数后会变成一个很小的数，
            # 而原来比它小的数在乘以同样的负数之后反而会变得比上面的结果大，
            # 所以正负号的不确定性就导致这里必须同时维护一个cur_max和cur_min

            cur_max = max(candidates)
            cur_min = min(candidates)
            final_max = max(final_max, cur_max)
            print(f'\ncandidates = {candidates}'
                  f'\ncur_max = {cur_max}, cur_min = {cur_min}'
                  f'\nfinal_max = {final_max}')
        
        return final_max


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, -2, 4]
    res = sol.maxProduct(nums)
    print(f'res = {res}')


"""Result:
candidates = (3, 6, 6)
cur_max = 6, cur_min = 3
final_max = 6

candidates = (-2, -12, -6)
cur_max = -2, cur_min = -12
final_max = 6

candidates = (4, -8, -48)
cur_max = 4, cur_min = -48
final_max = 6

res = 6
"""
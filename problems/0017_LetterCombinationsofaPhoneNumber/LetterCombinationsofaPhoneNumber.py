class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        
        # nums = set(list(digits)) 
        # 注意：这个地方不能去重，因为输出的是字母之间的排列组合，
        # 所以"222"和"2"得到的结果是不一样的

        # 直接转成list就行
        nums = list(digits)
        length = len(nums)
        print(f'nums = {nums}')
        
        # 注意：res的初始值不能写成[]，否则得到的结果永远是[]。
        # 因为写成[]会导致for循环根本就没进去，也就是代码就直接跳过了，
        # 而写成['']，则会进去读空字符串，使循环执行一轮。
        res = ['']

        for i in range(length):
            res = [tmp1+tmp2 for tmp1 in res for tmp2 in table[nums[i]]]

            # 注意：上面那个式子可以让输出结果直接等于res，没必要先让其等于cur，
            # 再让res=cur

            print(f'res = {res}')
        
        # 注意：在return的时候，题目要求输入为空字符串时输出[]而不是['']，
        # 因此对输出字符串为空必须单独处理。
        return [] if length == 0 else res
            
if __name__ == '__main__':
    sol = Solution()
    digits = "23"
    # digits = ""
    res = sol.letterCombinations(digits)
    print(f'res = {res}')


"""输出结果：
nums = ['2', '3']
res = ['a', 'b', 'c']
res = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
res = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""
import numpy as np

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the length first, which will be used later
        n = len(nums)
        
        # expand `nums`, add num 1 both in the head and in the tail
        nums.insert(0, 1) # insert() method: insert an element in the given position
        nums.append(1)
        
        # allocate a matrix for dp with shape (n+2, n+2)
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        
        """
        Attentions:
            1. The min value of length must be starting from 1, so length traversals from 1.
               And the max length surely is n, the size of nums.
            2. i is the left endpoint of area [i, j], since we insert a 1 to the left of nums, so i must be starting from 1.
               Then why does i end in n-length+1? Think that length = 1, then max(i)=n, that's right because the length of 
               the expanded `nums`is n+2, with the last element indexed n+1, but i cannot reach it because it is 1 we added
               to the tail before. So i can mostly reach the index n.
            3. j is the right endpoint of area [i, j], since the length of the area is determined, so j - i equals to an
               invariant number: length. That's why j = i + length - 1. (Why minus 1? Think that i = 1, length = 1, then 
               j = i + length = 2? That's false, we need to minus 1 to let j = 1.)
            4. k is a "traversor", it is used to traversal every area [i, j] from k=i to k=j, and calculate dp[i][j] based
               on k.
        """
        for length in range(1, n+1): # first recursive the area length from 1 to n
            for i in range(1, n-length+2): # second, recursive the area start
                j = i + length - 1 # j is set to the end of area [i, j]
                for k in range(i, j+1): # third, recursive k in area [i, j]
                    dp[i][j] = max(dp[i][j], 
                                   nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]) # state transforming equation
                    print(f"\ndp = \n{np.array(dp)}")
        
        return dp[i][n]

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 5, 8]
    res = sol.maxCoins(nums)
    print(res)


"""Result:
dp =
[[0 0 0 0 0 0]
 [0 3 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3  0  0  0  0]
 [ 0  0 15  0  0  0]
 [ 0  0  0  0  0  0]
 [ 0  0  0  0  0  0]
 [ 0  0  0  0  0  0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3  0  0  0  0]
 [ 0  0 15  0  0  0]
 [ 0  0  0 40  0  0]
 [ 0  0  0  0  0  0]
 [ 0  0  0  0  0  0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3  0  0  0  0]
 [ 0  0 15  0  0  0]
 [ 0  0  0 40  0  0]
 [ 0  0  0  0 40  0]
 [ 0  0  0  0  0  0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3 30  0  0  0]
 [ 0  0 15  0  0  0]
 [ 0  0  0 40  0  0]
 [ 0  0  0  0 40  0]
 [ 0  0  0  0  0  0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3 30  0  0  0]
 [ 0  0 15  0  0  0]
 [ 0  0  0 40  0  0]
 [ 0  0  0  0 40  0]
 [ 0  0  0  0  0  0]]

dp =
[[ 0  0  0  0  0  0]
 [ 0  3 30  0  0  0]
 [ 0  0 15 64  0  0]
 [ 0  0  0 40  0  0]
 [ 0  0  0  0 40  0]
 [ 0  0  0  0  0  0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30   0   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40   0   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30   0   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40  45   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30   0   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135   0   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135  51   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135  70   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159   0   0]
 [  0   0  15 135 159   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159 162   0]
 [  0   0  15 135 159   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159 162   0]
 [  0   0  15 135 159   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159 162   0]
 [  0   0  15 135 159   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

dp =
[[  0   0   0   0   0   0]
 [  0   3  30 159 167   0]
 [  0   0  15 135 159   0]
 [  0   0   0  40  48   0]
 [  0   0   0   0  40   0]
 [  0   0   0   0   0   0]]

res = 167
"""
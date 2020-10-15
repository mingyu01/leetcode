$O(n^2)$ 解法的思路：

- 需要提前申请一个 dp 数组。假设 `len(nums) = n` ，则提前申请一个长度为 n 且全为 1 的数组 dp；

- 内外两层循环，状态转移方程如下：

  ```python
  dp[i] = max(dp[i], dp[k] + 1)
  ```

  状态转移方程的触发条件是必须要满足 `nums[i] > nums[k]`

- 最终返回 `max(dp)`



****



$O(n\log n)$ 解法的思路：

参考：[https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation](https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation)



这里其实用到的是一种 grouping 思想：

- 假设我们现在的数组是：`[4, 5, 6, 3]` ，假如新来了一个数 `num` ，则先把现有的数组按如下规则进行 grouping：

- 先把所有长度为 1 的 LIS 挑出来，它们会形成一串列表：`[4], [5], [6], [3]` ；

- 再把所有长度为 2 的 LIS 挑出来，它们也会形成一串列表：`[4, 5], [5, 6]` ；

- 再把所有长度为 3 的 LIS 挑出来，形成一串列表：`[4, 5, 6]` ；

- 定义 `tails` 数组如下：当 LIS 的长度为 `k` 时，`tails[k-1]` 表示所有长度为 `k` 的 LIS 的最后一个元素中最小的那个元素，即：

  ```python
  k = 1, LISs = [[4], [5], [6], [3]], 
  tails[0] = min(LIS[-1] for LIS in LISs) = min(4, 5, 6, 3) = 3
  
  k = 2, LISs = [[4, 5], [5, 6]], 
  tails[1] = min(LIS[-1] for LIS in LISs) = min(5, 6) = 5
  
  k = 3, LISs = [[4, 5, 6]], 
  tails[2] = min(LIS[-1] for LIS in LISs) = min(6) = 6
  ```

- 我们最终想知道的是这个 `k` 最大到底能达到多大。那么当新来一个数 `num` 时，它会不会对这个 `k` 产生影响呢？这里边要分两种情况：

  - 第一种情况：假如目前最大的 `k` 等于 `k0` ，如果 `num > tails[k0-1]` ，那就说明新来的这个 `num` 比目前最长的 LIS 的最后一个数的值还大，这个时候 `num` 就可以接到这个最长的 LIS 的后面，从而使得目前最大的 `k` 值能够再加 1（即最长的 LIS 能够再增长 1 位）。
  - 第二种情况，如果 `num < tails[k0-1]` ，那就进行 binary search 找到要插入的位置，然后替换 `tails` 中相应位置处的元素。k 的最大值不变。

- 最终返回最大的 `k` 即可。
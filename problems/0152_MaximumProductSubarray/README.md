关于这一题的详细解释，参考：

- [https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity](https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity)



大体思想还是 dp，但是因为不知道新来的数据是正还是负，所以既要维护最大值 `cur_max` ，也要维护最小值 `cur_min` 。

同时，为了保证数组连续，每一个新来的 `nums[i]` 都必须要参与运算，只是它运算的结果不一定会被传递到下一个位置处。核心代码参见 `.py` 文件。
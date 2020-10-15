Summary：

|    Time    | No.  |               Problem                | Level  |                            Point                             |
| :--------: | :--: | :----------------------------------: | :----: | :----------------------------------------------------------: |
| 2020-10-14 | 312  |            Burst Ballons             |  Hard  | `dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j])` |
| 2020-10-14 |  17  | Letter Combinations of a PhoneNumber | Medium | `res = [tmp1+tmp2 for tmp1 in res for tmp2 in table[nums[i]]]` |
| 2020-10-14 | 128  |     Longest Consecutive Sequence     |  Hard  |       `if num-1 not in nums_set, while y in nums_set`        |
| 2020-10-15 | 300  |    Longest Increasing Subsequence    | Medium |     `if nums[i] > nums[k]: dp[i] = max(dp[i], dp[k]+1)`      |




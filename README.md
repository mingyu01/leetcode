Summary：

|    Time    | No.  |    Problem    | Level |                            Point                             |
| :--------: | :--: | :-----------: | :---: | :----------------------------------------------------------: |
| 2020-10-14 | 312  | Burst Ballons | Hard  | `dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j])` |


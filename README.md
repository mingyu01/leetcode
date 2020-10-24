Summary：

|    Time    | No.  |               Problem                | Level  |                            Point                             |
| :--------: | :--: | :----------------------------------: | :----: | :----------------------------------------------------------: |
| 2020-10-14 | 312  |            Burst Ballons             |  Hard  | `dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j])` |
| 2020-10-14 |  17  | Letter Combinations of a PhoneNumber | Medium | `res = [tmp1+tmp2 for tmp1 in res for tmp2 in table[nums[i]]]` |
| 2020-10-14 | 128  |     Longest Consecutive Sequence     |  Hard  |       `if num-1 not in nums_set, while y in nums_set`        |
| 2020-10-15 | 300  |    Longest Increasing Subsequence    | Medium |     `if nums[i] > nums[k]: dp[i] = max(dp[i], dp[k]+1)`      |
| 2020-10-15 | 200  |          Number of Islands           | Medium | `dfs: for k in range(4): if not visited[x_next][y_next] and grid[x_next][y_next] == '1': self.dfs(grid, visited, x_next, y_next, m, n)` |
| 2020-10-24 | 139  |              Word Break              | Medium | dp: `for i in range(1, n+1): for j in range(i): if dp[j] and s[j:i] in wordDict: dp[i] = True` |
| 2020-10-24 | 1143 |      Longest Common Subsequence      | Medium | `dp[i][j]: if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1 else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])` |



****

Git 操作：

```shell
# git add 后如何撤销某些文件(假如不小心add了 aaa.txt)：
git reset HEAD aaa.txt
```


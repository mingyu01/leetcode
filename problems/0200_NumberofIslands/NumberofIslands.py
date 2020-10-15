class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # 因为后面要用到 res += 1，所以先申请一个res，用来表示最后要返回
        # 的结果
        res = 0

        # 先判断特殊情况
        if len(grid) == 0:
            return res
        
        m, n = len(grid), len(grid[0])

        # visited = [[False for i in range(m)] for j in range(n)]
        # 注意：这里是先n后m，而不是先m后n，否则visited矩阵的维度就会出错
        visited = [[False for i in range(n)] for j in range(m)]
        
        # 两层for循环遍历矩阵中的每一个位置
        for i in range(m):
            for j in range(n):
                
                # 如果还没有被访问过并且是陆地
                if not visited[i][j] and grid[i][j] == '1':

                    # 这里dfs的目的是为了影响visited矩阵，dfs不需要返回
                    # 任何值
                    self.dfs(grid, visited, i, j, m, n)

                    # 把当前位置能污染的都污染之后，res加1
                    res += 1
        
        return res
        
    def dfs(self, grid, visited, i, j, m, n):

        # 进dfs之后，要做的第一件事就是先污染visited矩阵（即标记当前
        # 位置为“访问过”）
        visited[i][j] = True

        # 然后申请一个方向数组
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # 总共循环4轮
        for k in range(4):
            x_next = i + dx[k]
            y_next = j + dy[k]

            # 我们要在这个4轮的小循环中去开启下一个dfs，因此，就要在这个小循环
            # 中，提前把越界的情况过滤掉。
            # 注意：这里的判断条件只包含越界，不包含visited[x_next][y_next]
            # 是否已访问过。
            if x_next < 0 or x_next >= m or y_next < 0 or y_next >= n:
                continue
            
            # 在这个小循环中：
            # 如果当前位置没有访问过，并且当前位置为陆地，
            # 那就开启下一轮dfs。
            if not visited[x_next][y_next] and grid[x_next][y_next] == '1':
                self.dfs(grid, visited, x_next, y_next, m, n)



if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    res = sol.numIslands(grid)
    print(f'res = {res}')


"""
结果：res = 1
"""
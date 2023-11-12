# 扫雷游戏
# 要求，根据输入的click动作，返回之后的盘面
# 其中 M表示未挖出的地雷，E表示未挖出的空方块，B表示已挖出的空方块，数字表示周围地雷的数量，X表示已挖出的地雷
# 根据以下规则返回点击之后对应的盘面
# 1. 如果点击的是地雷，则将地雷改为X，返回
# 2. 如果是没有相邻地雷的空方块E，则将其改为B，然后递归的将其相邻的方块改为B
# 3. 如果是有相邻地雷的空方块，则将其修改为数字
# 4. 如果在此次点击中，无更多的方块被揭露，则返回盘面
import loguru
class Solution:
    def updateBoard(self, board, click):
        # 将原始棋盘转换成为 recover的形式
        # 同时计算点击下的连通图作为mask
        # 利用mask recovery的合体来实现最终的结果
        self.dirs = [[1,0], [-1,0], [0, 1], [0,-1],
                [1,1], [1,-1], [-1, 1], [-1, -1]]
        m = len(board)
        n = len(board[0])
        dp = [[0 for _ in range(n)] for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    dp[i][j] = -1
                    for dir in self.dirs:
                        if i+dir[0] >=0 and i+dir[0] < m and j+dir[1] >= 0 and j+dir[1] < n:
                            if dp[i+dir[0]][j+dir[1]] != -1:
                                dp[i+dir[0]][j+dir[1]]+=1   
        loguru.logger.info(dp)
        # 从click开始进行dfs，三种情况
        # 1. 如果是dp 地雷，将board中的M改为X，返回
        # 2. 如果是dp 数字，将board中的E改为数字，返回
        # 3. 如果是dp 中的0，将board中的E改为B，然后递归的将其相邻的方块改为B
        # loguru.logger.info(dp)
        if dp[click[0]][click[1]] == -1:
            board[click[0]][click[1]] = 'X'
            return board
        if dp[click[0]][click[1]] > 0:
            board[click[0]][click[1]] = str(dp[click[0]][click[1]])
            return board
        if dp[click[0]][click[1]] == 0:
            # 说明修改的是E
            print(board)
            self.dfs(dp,click[0],click[1])
            print(board)
            return board

    def dfs(self,dp,i,j):
        # loguru.logger.info('dfs')
        if i<0 or i>=len(dp) or j<0 or j>=len(dp[0]):
            loguru.logger.info('out of range')
            return 
        if dp[i][j] != 0:
            loguru.logger.info('not zero')
            board[i][j] = str(dp[i][j])
            print(board)
            return
        if dp[i][j] == 0 and board[i][j] == 'E':
            loguru.logger.info('zero')
            board[i][j] = 'B'
            print(board)
            for dir in self.dirs:
                self.dfs(dp,i+dir[0],j+dir[1])

board = [["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","M"],
         ["E","E","M","E","E","E","E","E"],
         ["M","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","M","M","E","E","E","E"]]
click = [0,0]
s = Solution()
print(s.updateBoard(board,click))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       #let us look at memorization approach-- top-down 
       # we will express the base cases and recursion in terms of indexes as first step
       # explore all the possibilites / count all ways
       # sum up the number of possibilites
        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # def path_rec(i,j,dp):
        #     if i==0 and j==0:
        #         dp[i][j] = 1
        #         return dp[i][j]
        #     # Note when we are counting ways or counting path, we will return a 1 on base case to keep the count.
        #     if dp[i][j]!=-1:
        #         return dp[i][j] 
        #     if i<0 or j<0:
        #         return 0 #For a failure that is going out of bounds or out of path, we will return a 0.
        #     # since we are going top-down, that is starting from the destination, we will take reverse directions, i.e go up and left

        #     #when we move up, we reduce the row index by 1
        #     #when we move left, we reduce the col index by 1

        #     up=path_rec(i-1,j,dp)
        #     left=path_rec(i,j-1,dp)
        #     dp[i][j]=up+left
        #     return dp[i][j]
        # return path_rec(m-1,n-1,dp)

        #Tabulation-> bottom up to get rid of recursion stack space 
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up,left=0,0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]
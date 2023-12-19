from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        #we can do it inplace using bit manipulation method
        #brute force solution=> in O(9*N*M)) OR just O(N*M) AND extra space for result matrix
        rows = len(img)
        cols = len(img[0])
        solution = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sum_mat = 0
                count = 0
                directions=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1],[0,0]]
                for direction in directions:
                    dr = direction[0] + i
                    dc = direction[1] + j

                    if 0 <= dr < rows and 0 <= dc < cols:
                        count += 1
                        sum_mat += img[dr][dc]

                solution[i][j] = sum_mat // count

        return solution

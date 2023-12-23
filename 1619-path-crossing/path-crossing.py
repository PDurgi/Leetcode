import collections

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        (row, col) = (0, 0)
        my_dict = collections.defaultdict(list)
        my_dict['N'].append((-1, 0))  # Adjusted direction vectors
        my_dict['E'].append((0, 1))
        my_dict['W'].append((0, -1))
        my_dict['S'].append((1, 0))

        visited.add((0, 0))
        for p in path:
            if p in my_dict.keys():
                row_change, col_change = my_dict[p][0]
                row += row_change
                col += col_change
                if (row, col) in visited:
                    return True
                visited.add((row, col))

        return False
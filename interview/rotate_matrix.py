import numpy as np

# def spiralOrder(matrix):
#     """
#     顺时针旋转数组
    
#     Params:
#         m: 矩阵的行
#         n: 矩阵的列
    
#     Returns:
#         返回二维数组顺时针旋转的结果
#     """
#     # return matrix.shape
#     matrix = np.array(matrix)
#     m = matrix.shape[0] 
#     n = matrix.shape[1]
#     l = m*n
#     if l == 1:
#         return matrix[0]
    
#     new_list = [0]*(l)

#     i = 0
#     row = 0
#     col = 0
#     circle = 0
    
#     while i < l:
#         #行不变，列加1
#         while col < n-(1+circle) and i < l:
#             new_list[i] = matrix[row][col]
#             # print(row, col, i, m, n, l)
#             col += 1
#             i += 1
        
#         #列不变，行+1
#         while row < m-(1+circle) and i < l:
#             new_list[i] = matrix[row][col]
#             # print(row, col, i, m, n, l)
#             row += 1
#             i += 1

#         #行不变，列-1
#         while col > (0+circle) and i < l:
#             new_list[i] = matrix[row][col]
#             # print(row, col, i, m, n, l)
#             # print('sss')
#             col -= 1
#             i += 1
#         #列不变，行-1
#         while row > (0+circle) and i < l:
#             new_list[i] = matrix[row][col]
#             # print(row, col, i, m, n, l)
#             row -= 1
#             i += 1
#         # print(row, col)
#         row += 1
#         col += 1
#         circle+=1

#         if i == l-1: 
#             new_list[i] = matrix[row][col]
#             break
#     return new_list

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix or not matrix[0]:
        return list()
    rows,cols = len(matrix),len(matrix[0])
 
    # visited = [[False] * cols] * rows
    visited = [[False] * cols for _ in range(rows)]
    total = rows * cols
    order = [0] * total
 
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    
    row,col = 0,0
    directionIndex = 0

    for i in range(total):
        order[i] = matrix[row][col]
        visited[row][col] = True
 
        next_row,next_col = row + directions[directionIndex][0], col + directions[directionIndex][1]
 
        if not (0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col]):
            directionIndex = (directionIndex + 1) % 4
        
        row = row + directions[directionIndex][0]
        col = col + directions[directionIndex][1]
        
    return order


    

# def spiralOrder(matrix):
#     if not matrix or not matrix[0]:
#         return list()
    
#     rows, columns = len(matrix), len(matrix[0])
#     visited = [[False] * columns for _ in range(rows)]
#     total = rows * columns
#     order = [0] * total

#     directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     row, column = 0, 0
#     directionIndex = 0
#     for i in range(total):
#         order[i] = matrix[row][column]
#         visited[row][column] = True
#         nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
#         if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
#             directionIndex = (directionIndex + 1) % 4
#         row += directions[directionIndex][0]
#         column += directions[directionIndex][1]
#     return order

    


if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    new_l = spiralOrder(matrix)
    print(new_l)
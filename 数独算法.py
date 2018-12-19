'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


'''
# false
board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

print(8 % 3)
print([i[0] for i in board].count('8'))


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 思路一：复杂的分条判断   76ms
#         for i in range(9):
#             if 9 - len(set(board[i])) != board[i].count(".") - 1:     # 条件一
#                 return False

#             new_list = []                                                       
#             for j in range(9):                                         # 条件二
#                 if board[j][i] != '.' and board[j][i] in new_list:
#                     return False
#                 if board[j][i] != '.' and board[j][i] not in new_list:         
#                     new_list.append(board[j][i])    


#         aa,bb = [0,3,6],[0,3,6]
#         for a in aa:                    # 条件三
#             for b in bb:
#                 new_list = []
#                 for i in range(a,a+3):                
#                     for j in range(b,b+3):
#                         if board[i][j] != '.' and board[i][j] in new_list:
#                             return False
#                         if board[i][j] != '.' and board[i][j] not in new_list:         
#                             new_list.append(board[i][j])

#         return True



        # 思路二： 只循环一次完成数据的分类，用存储空间来换取算法的效率（借鉴）。

#         dic_row = [{},{},{},{},{},{},{},{},{}]            # 每行的元素以一个字典储存，key是数字，value统一为1.
#         dic_col = [{},{},{},{},{},{},{},{},{}]
#         dic_box = [{},{},{},{},{},{},{},{},{}]

#         for i in range(len(board)):
#             for j in range(len(board)):
#                 num = board[i][j]
#                 if num == ".":
#                     continue
#                 if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
#                     dic_row[i][num] = 1
#                     dic_col[j][num] = 1
#                     dic_box[3*(i//3)+(j//3)][num] = 1       # 利用地板除，向下取余。巧妙地将矩阵划分为九块
#                 else:
#                     return False

#         return True




        # 思路三： 思路二的另一种实现方式。代码更为简洁（借鉴）
        Cell = [[] for i in range(9)]                   # 没有必要用dict,我们只某个数字关心有没有出现过
        Col =  [[] for i in range(9)]
        Row =  [[] for i in range(9)]

        for i,row in enumerate(board):                  # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for j,num in enumerate(row):
                if num != '.':
                    k = (i//3)*3 + j//3
                    if num in Row[i] + Col[j] + Cell[k]:    # list的骚操作,将三个list顺序的拼接 
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)

        return True



# 方法一
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)



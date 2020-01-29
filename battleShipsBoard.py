#LC 419 : Battleships in board

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        total_ships = 0
        for i in range(len(board)):
            print(board[i])
            for j in range(len(board[i])):
                if board[i][j] == "X":  # only if element is "X", we check next element and element above it 
                    ships = 1
                    if j > 0 and board[i][j-1] == "X":   # check neighbors: if atleast second element of row, check that row's previous element
                        ships = 0 
                        print(board[i][j-1])
                    if i > 0 and board[i-1][j] == "X":   # check upper neighbors: if atleast second coloumn, check element above found "X"
                        ships = 0
                    total_ships += ships
        return total_ships
        



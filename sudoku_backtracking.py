import copy
from data import sudoku1, sudoku2

class Sudoku:
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board

    def _is_x_valid(self, number: int, position: int) -> bool:
      return not any(self.board[position][column] == number for column in range(9))
    
    def _is_y_valid(self, number: int, position: int) -> bool:
        return not any(self.board[row][position] == number for row in range(9))
    
    def _is_section_valid(self, number: int, x: int, y: int) -> bool:
        section_x, section_y = (x // 3) * 3, (y // 3) * 3

        return not any(
            self.board[row][column] == number
            for row in range(section_y, section_y + 3)
            for column in range(section_x, section_x + 3)
            if (row, column) != (y, x) # current row and column are checked for `_is_[x | y]_valid` method
        )

    def _is_valid(self, number: int, y: int, x: int) -> bool:
        return self._is_x_valid(number, y) and self._is_y_valid(number, x) and self._is_section_valid(number, x, y)

    def solve(self, row: int = 0, column: int = 0):
        if row == 9: return True # sudoku is solved if row  > 8
        if column == 9: return self.solve(row + 1, 0) # move to the next row
        if self.board[row][column]: return self.solve(row, column + 1) # skip filled cells

        for number in range (1, 10):
            if not self._is_valid(number, row, column): continue
            self.board[row][column] = number
            if self.solve(row, column + 1): return True
            self.board[row][column] = 0 # backtrack
        return False


def print_sudoku(name: str, sudoku: list[list[int]], output: list[list[int]]) -> None:
    print('\n')
    print(name)
    for x in range(9):
        print(f'{sudoku[x]} \t {output[x]}')
    print('\n')

if __name__ == "__main__":
    print('\n')
    sudoku = Sudoku(copy.deepcopy(sudoku1))
    sudoku.solve()
    print_sudoku('Sudoku 1', sudoku1, sudoku.board)

    sudoku = Sudoku(copy.deepcopy(sudoku2))
    sudoku.solve()
    print_sudoku('Sudoku 2', sudoku2, sudoku.board)



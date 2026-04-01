class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board)
        row_count = [set() for _ in range(board_length)]
        column_count = [set() for _ in range(board_length)]
        square_count = [[set(), set(), set()] for _ in range(3)]

        for i in range(board_length):
            for j in range(board_length):

                print(f"square number: {i//3} {j//3}")

                current_number = board[i][j]
                if current_number == ".":
                    continue

                # row checking
                if current_number not in row_count[i]:
                    row_count[i].add(current_number)
                else:
                    return False

                # column checking
                if current_number not in column_count[j]:
                    column_count[j].add(current_number)
                else:
                    return False
                
                if current_number not in square_count[i//3][j//3]:
                    square_count[i//3][j//3].add(current_number)
                else:
                    return False


        print(row_count)
        


        return True
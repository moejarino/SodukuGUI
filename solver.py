# solver.py

def solve(bo):
    # return row and column of empty square
    find = find_empty(bo)
    # Base case of recursion is a full board, the board is solved
    if not find:
        return True
    else:
        row, col = find

    # We call valid, we are checking the empty positions in the board given from find with 1-10
    for i in range(1,10):
        # if valid add them to the board
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # Call solve again on the board with the new value added
            if solve(bo):
                return True

            bo[row][col] = 0
    # If we loop through 1-9 and none of them are valid, then we return false
    # We reset the last element we tried to add to an empty square
    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        # Now we check each column or element in this row.
        # Is it equal to the number we put in and make sure not to check same position
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        # Check every row or element in each columns
        # and make sure the number is not the same or its not in the same position we just entered
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # This divides the board into 9 sub boxes. The top left box is 0,0 then to the right 1,0...
    # If pos is (4,0), then 4//3 is 1 and 0//3 is 0. So bo 1,0
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # box nums can only be 0, 1, or 2. SO to check through the board elements, we need to
    # multiply by 3 to get to the actual index of the board. And we add three to capture
    # the rest of the box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


# def print_board(bo):
#     for i in range(len(bo)):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - - - ")

#         for j in range(len(bo[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")

#             if j == 8:
#                 print(bo[i][j])
#             else:
#                 print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

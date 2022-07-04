#Backtracking

#Algorithm: 

# 2. Create a recursive function
# 3. Search for any unassigned location
# 1. Verify if the "movement" is permitted or not
# 4. If all possibles "movement" are done return True

# Is considered a empty_location the num that equal a 0
def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False


def used_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False


def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if grid[row+i][col+j] == num:
                return True
    return False


def isSafe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, 
    row-row%3, 
    col-col%3, 
    num)


def solveSudoku(grid):
    l = [0,0]

    if(not find_empty_location(grid, l)):
        return True
    
    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if(isSafe(grid, row, col, num)):
            grid[row][col] = num

            if solveSudoku(grid):
                return True
            
            grid[row][col] = 0
    
    return False

def printing(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
        print()

if __name__ == "__main__":

    grid =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 0, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    
    if (solveSudoku(grid)):
        printing(grid)
    else:
        print(-1)
    
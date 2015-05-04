def check_sudoku(p):
    n = len(p) #Extract size of grid
    digit = 1 #start with 1
    while digit <= n: #Go through each digit
        i = 0
        while i < n: #Go through each row and column
            row_count = 0
            col_count = 0
            while j < n: #for each entry in ith row/column
                if p[i][j] == digit: #check row count
                    row_count += 1
                if p[j][i] == digit: #check column count
                    col_count += 1
                j += 1
            if row_count != 1 or col_count != 1: #check out the digit in maze
                return False
            i += 1 #next row/column
        digit += 1
    return True #Nothing was wrong!

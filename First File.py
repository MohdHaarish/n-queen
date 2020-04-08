closedlist = []
history = {0: (0, 0)}
n = 0


def checkifAlready(arr, ti, tj):
    #print("In checkifalready function")
    #print("Before 1")
    for j3 in range(tj + 1, n):
        if arr[ti][j3] == 1:
            return 0
    #print("Before 2")
    for j4 in range(0, tj):
        if arr[ti][j4] == 1:
            return 0
    #print("Before 3")
    for i in range(ti + 1, n):
        if arr[i][tj] == 1:
            return 0
    #print("Before 4")
    for i in range(0, ti):
        if arr[i][tj] == 1:
            return 0
    #print("Before 5")
    for i1 in range(n):
        for j5 in range(n):
            if ti-i1 == tj-j5:
                if arr[i1][j5] == 1:
                    return 0
    for i2 in range(n):
        for j6 in range(n):
            if ti-i2 == -(tj-j6):
                if arr[i2][j6] == 1:
                    return 0
    #print("Exiting check if function")
    return 1


def printthegrid(grid):
    #print("In print grid function")
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()

def makegridnull(grid):
    for i in range(n):
        for j1 in range(n):
            grid[i][j1] = 0

def createGrid(i1, j2, grid1, totalqueens1):
    #print("In create grid function")
    #print(n)
    closedlist.append((i1, j2))
    grid1[i1][j2] = 1
    #print("At total queens: ", totalqueens1)
    #print("i: ", i1, ", j: ", j2)
    '''for i2 in range(n):
        for j3 in range(n):
            print(grid1[i2][j3], ' ', end='')
        print("")'''
    if totalqueens1 == n:
        return 1

    #print("Before 1")
    #print("i: ",i1 ,", j2: ",j2)
    for i in range(i1+1, n):
        for j1 in range(j2+2, n):
      #      print("---In 1, i: ", i, ' ', j1)
            if i < n and j1 < n:
     #           print("In 1, i: ",i,' ',j1)
                if checkifAlready(grid1, i, j1) == 1:
                    if createGrid(i, j1, grid1, (totalqueens1 + 1)) == 1:
                        return 1
                    else:
                        grid1[i][j1] = 0
    #print("Before 2")
    #print(i + 2 < n and j1 + 1 < n)
    for i2 in range(i1+2, n):
        for j3 in range(j2+1, n):
      #      print("---In 2, i: ", i2, ' ', j3)
            if i2 < n and j3 < n:
     #           print("In 2, i: ",i2,' ',j3)
                if checkifAlready(grid1, i2, j3) == 1:
                    if createGrid(i2, j3, grid1, (totalqueens1 + 1)) == 1:
                        return 1
                    else:
                        grid1[i2][j3] = 0
    #print("Before 3")
    #print(i + 1 < n and j1 - 2 >= 0)
    for i3 in range(i1+1, n):
        for j4 in range(j2-2, -1, -1):
      #      print("---In 3, i: ", i3, ' ', j4)
            if i3 < n and j4 >= 0:
     #           print("In 3,i: ",i3,' ',j4)
                if checkifAlready(grid1, i3, j4) == 1:
                    if createGrid(i3, j4, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i3][j4] = 0
    #print("Before 4")
    #print(i - 2 >= 0 and j1 + 1 < n)
    for i4 in range(i1-1, -1, -1):
        for j5 in range(j2+1, n):
      #      print("---In 4, i: ", i4, ' ', j5)
            if i4 >= 0 and j5 < n:
     #           print("In 4,i: ",i4,' ',j5)
                if checkifAlready(grid1, i4, j5) == 1:
                    if createGrid(i4, j5, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i4][j5] = 0
    #print("Before 5")
    #print(i - 1 >= 0 and j1 + 2 < n)
    for i5 in range(i1-1, -1, -1):
        for j6 in range(j2+2, n):
      #      print("---In 5, i: ", i5, ' ', j6)
            if i5 >= 0 and j6 < n:
     #           print("In 5,i: ",i5,' ',j6)
                if checkifAlready(grid1, i5, j6) == 1:
                    if createGrid(i5, j6, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i5][j6] = 0
    #print("Before 6")
    #print(i + 2 < n and j1 - 1 >= 0)
    for i6 in range(i1+2, n):
        for j7 in range(j2-1, -1, -1):
      #      print("---In 6, i: ", i6, ' ', j7)
            if i6 < n and j7 >= 0:
     #           print("In 6, i: ",i6,' ',j7)
                if checkifAlready(grid1, i6, j7) == 1:
                    if createGrid(i6, j7, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i6][j7] = 0
    #print("Before 7")
    #print(i - 1 >= 0 and j1 - 2 >= 0)
    for i7 in range(i1-1, -1, -1):
        for j8 in range(j2-2, -1, -1):
      #      print("---In 7, i: ", i7, ' ', j8)
            if i7 >= 0 and j8 >= 0:
     #           print("In 7, i: ",i7,' ',j8)
                if checkifAlready(grid1, i7, j8) == 1:
                    if createGrid(i7, j8, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i7][j8] = 0
    #print("Before 8")
    #print(i - 2 >= 0 and j1 - 1 >= 0)
    for i8 in range(i1-2, -1, -1):
        for j9 in range(j2-1, -1, -1):
      #      print("---In 8, i: ", i8, ' ', j9)
            if i8 >= 0 and j9 >= 0:
     #           print("In 8, I: ",i8,' ',j9)
                if checkifAlready(grid1, i8, j9) == 1:
                    if createGrid(i8, j9, grid1, totalqueens1 + 1) == 1:
                        return 1
                    else:
                        grid1[i8][j9] = 0
    #print("After if")
    grid1[i1][j2] = 0
    return 0


if __name__ == "__main__":
    n = int(input("Enter the matrix size: "))
    grid = [[0] * n for i in range(n)]
    totalqueens = 0
    for i in range(n):
        for j in range(n):
            print(grid[i][j], ' ', end='')
        print("")
    original_list = [(0, 0), (0, 1)]
    for i, j in original_list:
        if createGrid(i, j, grid, totalqueens + 1) == 1:
            printthegrid(grid)
            break
        else:
            makegridnull(grid)

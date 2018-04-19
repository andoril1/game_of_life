from time import sleep

initialGrid = [
        ['.', 8, '.', '.', '.', '.', '.'],
        ['.', '.', 8, '.', '.', '.', '.'],
        [8, 8, 8, '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
       ]

def main(grid):
    print("Generation 0:")
    printGrid(grid)

    for i in range(18):
        grid = getNewGrid(grid)
        sleep(0.5)
        print("Generation " + str(i + 1) + ":")
        printGrid(grid)

def printGrid(grid):
    for i in range(len(grid)):
        
        for ii in range(len(grid[i])):
            
            print(grid[i][ii], end=' ', flush=True)

        print('')

def getNewGrid(grid):
    newGrid = []

    for y in range(len(grid)):
        row = []

        for x in range(len(grid[y])):
           row.append(getCellStatus(grid, y, x))

        newGrid.append(row)

    return newGrid

def getCellStatus(grid, yPosition, xPosition):
    if cellIsAlive(grid[yPosition][xPosition]):
        if hasLessThanTwo(grid, yPosition, xPosition) or hasMoreThanThree(grid, yPosition, xPosition):
            return '.'

        else:
            return 8

    else:
        if hasThree(grid, yPosition, xPosition):
            return 8

        else:
            return '.'

def cellIsAlive(cell):
    return cell == 8

def hasLessThanTwo(grid, yPosition, xPosition):
    aliveCount = getAliveNeighbours(grid, yPosition, xPosition)

    return aliveCount < 2

def hasMoreThanThree(grid, yPosition, xPosition):
    aliveCount = getAliveNeighbours(grid, yPosition, xPosition)

    return aliveCount > 3

def hasThree(grid, yPosition, xPosition):
    aliveCount = getAliveNeighbours(grid, yPosition, xPosition)

    return aliveCount == 3

def getAliveNeighbours(grid, yPosition, xPosition):
    counter = 0
    height = len(grid)
    width = len(grid[0])

    for y in [yPosition - 1, yPosition, yPosition + 1]:

        for x in [xPosition - 1, xPosition, xPosition + 1]:

            if ((y == yPosition and x == xPosition) or 
                x < 0 or y < 0 or y > height - 1 or x > width - 1):
                continue

            if cellIsAlive(grid[y][x]):
                counter += 1

    return counter

main(initialGrid)

#https://automatetheboringstuff.com/2e/chapter4/
#bottom practice project

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

#loop through each column in the first row

for col in range(len(grid[0])):
    #loop through each row of columns
    for row in range(len(grid)):
        print(grid[row][col], end='')
    #print newline at end of each row
    print()  
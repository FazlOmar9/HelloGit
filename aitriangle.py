#This program prints the shape of an equilateral triangle using 'A's

#Store the number of rows (height) and columns (width) of the triangle in variables
rows = 15
columns = 15

#Use a for loop to iterate through the number of rows
for i in range(rows):
    #Use a nested for loop to iterate through the number of columns
    for j in range(columns):
        #Use an if statement to determine when to print 'A'
        if (j > 0 and j < 14) and (i > 0 and i < 14):
            if j >= (rows - i - 1) and j <= i:
                print('A', end='')
            else:
                print(' ', end='')
        else:
            print(' ', end='')
    #Print a new line after each row
    print()
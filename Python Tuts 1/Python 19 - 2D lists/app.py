#2-D list is a list containing a set of lists
#TAKE
#a matrixrepresentation of a 2D_list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#as seen, each list in the main list represents a row

#accessing the members in the list
#you first call out the sublits in the main list, then you call out the member of that list
#That is, you use two SQUARE brackets

print(matrix[1][2])

#can also be modified using the same syntax
matrix[2][1] = 6
print(matrix)

#to itereate over the whole list, you can use for loops/nested loops
for sub_list in matrix:
    for members in sub_list:
        print(members)

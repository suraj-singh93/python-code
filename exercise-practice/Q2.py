# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def matrix_return(rows,columns):
    if rows == 0 or columns == 0:
        return None
    matrix_list = []
    for row in range(rows):
        temp_list = []
        for col in range(columns):
            temp_list.append(row*col)
        matrix_list.append(temp_list)

    return matrix_list

if __name__ == "__main__":
    print(matrix_return(4,5))



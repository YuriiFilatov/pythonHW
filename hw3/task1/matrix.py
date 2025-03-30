#!/usr/bin/env python3
import numpy 

class Matrix: 
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            raise ValueError("Ошибка размерностей матриц")
    
        sum = []
        for i in range(self.columns):
            row_sum = []
            for j in range(self.rows):
                row_sum.append(self.data[i][j] + other.data[i][j])
            sum.append(row_sum)
        
        return Matrix(sum)
    
    def __mul__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            raise ValueError("Ошибка размерностей матриц")
    
        mul = []
        for i in range(self.columns):
            row_mul = []
            for j in range(self.rows):
                row_mul.append(self.data[i][j] * other.data[i][j])
            mul.append(row_mul)
        
        return Matrix(mul)
    
    def __matmul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Ошибка размерностей матриц")
    
        matmul = []
        for i in range(self.rows):
            row_matmul = []
            for j in range(other.columns):
                sum = 0
                for k in range(self.columns):
                    sum += self.data[i][k] * other.data[k][j] 
                row_matmul.append(sum)
            matmul.append(row_matmul)
        
        return Matrix(matmul)
    
    def __str__(self):
        matrix_view = ""
        for row in self.data:
            matrix_view += "   ".join(str(elem) for elem in row) + '\n'          
        return matrix_view
    
if __name__ == "__main__":
    numpy.random.seed(0)
    matrix1 = Matrix(numpy.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(numpy.random.randint(0, 10, (10, 10)).tolist())

    sum = matrix1 + matrix2
    mul = matrix1 * matrix2
    matmul = matrix1 @ matrix2

    with open("matrix1.txt", "w", encoding="utf-8") as f_matrix1:
        f_matrix1.write(str(matrix1))

    with open("matrix2.txt", "w", encoding="utf-8") as f_matrix2:
        f_matrix2.write(str(matrix2))

    with open("matrix+.txt", "w", encoding="utf-8") as f_sum:
        f_sum.write(str(sum))

    with open("matrix*.txt", "w", encoding="utf-8") as f_mul:
        f_mul.write(str(mul))

    with open("matrix@.txt", "w", encoding="utf-8") as f_matmul:
        f_matmul.write(str(matmul))


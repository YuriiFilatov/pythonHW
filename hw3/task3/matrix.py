#!/usr/bin/env python3
import numpy 

global cache

cache = {}

class HashMixin:
    def __hash__(self):
        hash = 1
        for row in self.data:
            for elem in row:
                hash = hash * elem
        return hash
    
class Matrix(HashMixin): 
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
        global cache
        unique_hash = str(hash(self)) + '_' + str(hash(other))

        if unique_hash in cache:
            return type(self)(cache[unique_hash])
        
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
        
        cache[unique_hash] = matmul
        return Matrix(matmul)
    
    def __str__(self):
        matrix_view = ""
        for row in self.data:
            matrix_view += "   ".join(str(elem) for elem in row) + '\n'          
        return matrix_view
    
if __name__ == "__main__":
    cache = {}
    numpy.random.seed(0)
    matrixA = Matrix([[1, 2], [3, 4]])
    matrixC = Matrix([[1, 4], [2, 3]])
    matrixB = Matrix([[1, 1], [1, 1]])
    matrixD = Matrix([[1, 1], [1, 1]])

    with open("A.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixA))
    
    with open("B.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixB))

    with open("C.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixC))

    with open("D.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixD))

    with open("AB.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixA @ matrixB))
    
    assert hash(matrixA) == hash(matrixC)

    cache.clear()

    with open("CD.txt", "w", encoding="utf-8") as f:
        f.write(str(matrixC @ matrixD))

    cache.clear()
    hash1 = str(hash(matrixA @ matrixB))
    cache.clear()
    hash2 = str(hash(matrixC @ matrixD))

    with open("Hash.txt", "w", encoding="utf-8") as f:
        f.write(hash1  + "\n" + hash2)

    assert (matrixA @ matrixB).data == (matrixC @ matrixD).data




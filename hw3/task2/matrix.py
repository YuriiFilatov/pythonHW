import numpy

class ArithmMixin:
    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data + other._data)
        else:
            return type(self)(self._data + other)
    
    def __sub__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data - other._data)
        else:
            return type(self)(self._data - other)
    
    def __mul__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data * other._data)
        else:
            return type(self)(self._data * other)
    
    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data / other._data)
        else:
            return type(self)(self._data / other)
        
    def __matmul__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data @ other._data)
        else:
            raise ValueError("Несовпадение по типам")
        
class FileMixin:
    def save_file(self, name):
        numpy.savetxt(name, self._data.round(2), "%.4f")

class ViewMixin:
    def __str__(self):
        rows = []
        for row in self._data:
            row_str = " ".join(f"{val}" for val in row) 
            rows.append(row_str) 
        return "\n".join(rows) + "\n"

class GetSetMixin:
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, val):
        self._data = numpy.array(val)

class Matrix(ArithmMixin, FileMixin, ViewMixin, GetSetMixin):
    def __init__(self, array):
        self._data = numpy.array(array)

if __name__ == '__main__':
    numpy.random.seed(0)
    matrix1 = Matrix(numpy.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(numpy.random.randint(0, 10, (10, 10)))

    sum = matrix1 + matrix2
    mul = matrix1 * matrix2
    matmul = matrix1 @ matrix2

    sum.save_file("matrix+.txt")
    mul.save_file("matrix*.txt")
    matmul.save_file("matrix@.txt")

    print(str(sum))
    print(str(mul))
    print(str(matmul))




    
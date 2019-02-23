class Matrix:
   
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._values = [[0]*columns for i in range(rows)]
    
    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def values(self):
        return self._values

    def dot(self, other):
        if (self.columns != other.rows):
            raise ValueError("Row count of input matrix must match column count of this matrix")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.values[i][j] += self._values[i][k]*other.values[k][j]
        return result

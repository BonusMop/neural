import unittest
import linalg.matrix as lam
from math import exp

class TestMatrix(unittest.TestCase):

    def test_initMatrix(self):
        # arrange
        rows = 3
        columns = 4
        # act
        m = lam.Matrix(rows,columns)
        # assert
        self.assertEqual(m.rows,rows)
        self.assertEqual(m.columns,columns)
    
    def test_assignValues(self):
        # arrange
        num_rows = 3
        num_columns = 2
        m = lam.Matrix(num_rows, num_columns)
        # act
        for row in range(num_rows):
            for column in range(num_columns):
                m.values[row][column] = (row+1)*(column+1)
        # assert
        self.assertEqual(m.values[0][0], 1)
        self.assertEqual(m.values[2][1], 6)
    
    def test_dotThrowsWithDimensionMismatch(self):
        # arrange
        m1 = lam.Matrix(3, 2)
        m2 = lam.Matrix(5, 1)
        # act
        # assert
        with self.assertRaises(ValueError) as context:
            m1.dot(m2)
        self.assertEqual(str(context.exception),"Row count of input matrix must match column count of this matrix")
        
    def test_dotProduct(self):
        # arrange
        m1 = lam.Matrix(2,3)
        m1.values[0] = [-1,8,3]
        m1.values[1] = [12,4,0]
        m2 = lam.Matrix(3,1)
        m2.values[0] = [-1]
        m2.values[1] = [0]
        m2.values[2] = [1]
        # act
        result = m1.dot(m2)
        # assert
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.columns, 1)
        self.assertEqual(result.values[0][0],4)
        self.assertEqual(result.values[1][0],-12)
    
    def test_addThrowsWhenSizesDiffer(self):
        # arrange
        m1 = lam.Matrix(1,5)
        m2 = lam.Matrix(5,1)
        # act
        # assert
        with self.assertRaises(ValueError) as context:
            m3 = m1 + m2
        self.assertEqual(str(context.exception),"Dimensions of matrices must match in order to add")

    def test_addTwoMatrices(self):
        # arrange
        m1 = lam.Matrix(3,2)
        m1.values[0] = [1,2]
        m1.values[1] = [3,4]
        m1.values[2] = [5,6]
        m2 = lam.Matrix(3,2)
        m2.values[0] = [2,3]
        m2.values[1] = [4,5]
        m2.values[2] = [6,7]
        # act
        m3 = m1 + m2
        # assert
        self.assertEqual(m3.values[0][0],3)
        self.assertEqual(m3.values[0][1],5)
        self.assertEqual(m3.values[1][0],7)
        self.assertEqual(m3.values[1][1],9)
        self.assertEqual(m3.values[2][0],11)
        self.assertEqual(m3.values[2][1],13)

    def test_exponential(self):
        # arrange
        m = lam.Matrix(2,2)
        m.values[0] = [3,10]
        m.values[1] = [-5,0]
        # act
        result = m.exp()
        # assert
        self.assertEqual(result.values[0][0], exp(3))
        self.assertEqual(result.values[0][1], exp(10))
        self.assertEqual(result.values[1][0], exp(-5))
        self.assertEqual(result.values[1][1], exp(0))
    
    def test_negate(self):
        # arrange
        m = lam.Matrix(1, 3)
        m.values[0] = [2,-8,0]
        # act
        result = -m
        # assert
        self.assertEqual(result.values[0][0], -2)
        self.assertEqual(result.values[0][1], 8)
        self.assertEqual(result.values[0][2], 0)

if __name__ == '__main__':
    unittest.main()
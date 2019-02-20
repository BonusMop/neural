import unittest
import linalg.matrix as lam

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

if __name__ == '__main__':
    unittest.main()
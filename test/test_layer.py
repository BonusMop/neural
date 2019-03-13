import unittest
import network.layer as netl
import linalg.matrix as lam

class TestLayer(unittest.TestCase):

    def test_initLayer(self):
        # Arrange
        size = 12
        # Act
        l = netl.Layer(size)
        # Assert
        self.assertEqual(l.count,size)

    def test_weightsAndBiasesWhenPredecesor(self):
        # Arrange
        first_size = 5
        second_size = 10
        # Act
        first_layer = netl.Layer(first_size)
        second_layer = netl.Layer(second_size, first_layer)
        # Assert
        self.assertIsNone(first_layer.biases)
        self.assertIsNone(first_layer.weights)
        self.assertEqual(second_layer.biases.columns, 1)
        self.assertEqual(second_layer.biases.rows, second_size)
        self.assertEqual(second_layer.weights.columns, second_size)
        self.assertEqual(second_layer.weights.rows, first_size)
    
    def test_sigmoid(self):
        # Arrange
        l = netl.Layer(3)
        z = lam.Matrix(1,3)
        z.values[0] = [-4.0, 0.0, 2.5]
        # Act
        result = l.sigmoid(z)
        # Assert
        self.assertAlmostEqual(result.values[0][0], 0.0179, 3)
        self.assertAlmostEqual(result.values[0][1], 0.5, 3)
        self.assertAlmostEqual(result.values[0][2], 0.9241, 3)
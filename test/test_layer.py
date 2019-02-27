import unittest
import network.layer as netl

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
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

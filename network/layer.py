import linalg.matrix as lam

class Layer:

    def __init__(self,size,predecessor=None):
        self._count = size
        self._biases = None
        self._weights = None
        if (predecessor != None):
            self._biases = lam.Matrix(size, 1)
            self._weights = lam.Matrix(predecessor.count, size)
        return

    @property
    def count(self):
        return self._count

    @property
    def biases(self):
        return self._biases
    
    @property
    def weights(self):
        return self._weights

    def sigmoid(self, z):
        return ((-z).exp() + 1).reciprocal()
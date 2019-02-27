class Layer:

    def __init__(self,size):
        self._count= size
        return

    @property
    def count(self):
        return self._count
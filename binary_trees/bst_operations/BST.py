class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def get_right(self):
        return self._right

    def get_left(self):
        return self._left

    def get_data(self):
        return self._data

    def set_right(self, node):
        self._right = node

    def set_left(self, node):
        self._right = node

    def __str__(self):
        return str(self._data)

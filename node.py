import grid

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        
        if parent is None:
            self._depth = 0
        else:
            self._depth = parent.depth + 1

    def __str__(self):
        return str(self.state)

    @property
    def depth(self):
        return self._depth

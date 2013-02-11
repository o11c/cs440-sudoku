''' Representation of a Sudoku puzzle.
'''

from cell import Cell

class Grid(object):
    ''' An NN * NN sudoku state. It may be complete or incomplete

        Grid(3, string-of-length-81)
        Grid(4, iterable-of-256-cells)
    '''
    __slots__ = ('_a', '_n')

    def __init__(self, n, a):
        self._n = n
        self._a = tuple([Cell(x) for x in a])
        assert len(self._a) == n * n * n * n

    def __getitem__(self, indices):
        x, y = indices
        w = self._n * self._n
        return self._a[w * y + x]

    def __repr__(self):
        return 'Grid(%r, %r)' % (self._n, ''.join(str(x) for x in self._a))

    @property
    def n(self):
        return self._n

    def neighbors(self, x, y):
        if self[x, y]:
            yield self
            return
        raise NotImplementedError

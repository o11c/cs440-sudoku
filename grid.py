''' Representation of a Sudoku puzzle.
'''

import operator

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
        assert len(self._a) == self.nnnn
        for c in self._a:
            assert c.i <= self.nn

    def __getitem__(self, indices):
        x, y = indices
        w = self.nn
        return self._a[w * y + x]

    def row(self, x):
        nn = self.nn
        return self._a[nn*x : nn*x+nn]

    def col(self, y):
        nn = self.nn
        nnnn = nn * nn
        return self._a[y : y+nnnn : nn]

    def square(self, x, y):
        n = self._n
        return tuple(
                tuple(
                    self[i, j]
                        for j in range(y * n, y * n + n)
                )
                    for i in range(x * n, x * n + n)
        )

    def __str__(self):
        nn = self.nn
        return '\n'.join(
            ''.join(
                ' %s' % self[i, j]
                    for i in range(nn)
            )
                for j in range(nn)
        )

    def __repr__(self):
        return 'Grid(%r, %r)' % (self._n, ''.join(str(x) for x in self._a))

    @property
    def n(self):
        return self._n

    @property
    def nn(self):
        n = self._n
        return n * n

    @property
    def nnnn(self):
        n = self._n
        nn = n * n
        return nn * nn

    def replace(self, x, y, cv):
        ci = self.nn * y + x
        return Grid(self._n, self._a[:ci] + (cv,) + self._a[ci + 1:])

    def neighbors(self, x, y):
        if self[x, y]:
            yield self
            return
        for v in range(self.nn):
            v = Cell(v+1)
            if v in self.row(y):
                continue
            if v in self.col(x):
                continue
            if v in reduce(operator.add, self.square(x // self._n, y // self._n)):
                continue
            yield self.replace(x, y, v)

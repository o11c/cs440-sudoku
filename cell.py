''' Basic structure
'''

class Cell(object):
    ''' A cell represents a single number or blank

        A cell is immutable.

        Cell(s, i): define a new cell
        Cell(s) return a cached cell
    '''
    __cache = {}
    __slots__ = ('_s', '_i')

    def __new__(cls, s, i=None):
        if i is None:
            return Cell.__cache[s]
        c = object.__new__(cls)
        Cell.__cache[s] = c
        return c

    def __init__(self, s, i=None):
        if i is None:
            return
        assert isinstance(s, str)
        assert isinstance(i, int)
        self._s = s
        self._i = i

    def __bool__(self):
        return self._i
    __nonzero__ = __bool__

    @property
    def s(self):
        return self._s

    @property
    def i(self):
        return self._i

    def __str__(self):
        return self._s

    def __repr__(self):
        return 'Cell(%r, %r)' % (self._i, self._s)

Cell(' ', 0)
Cell('1', 1)
Cell('2', 2)
Cell('3', 3)
Cell('4', 4)
Cell('5', 5)
Cell('6', 6)
Cell('7', 7)
Cell('8', 8)
Cell('9', 9)

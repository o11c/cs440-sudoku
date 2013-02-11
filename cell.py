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
Cell('a', 10)
Cell('b', 11)
Cell('c', 12)
Cell('d', 13)
Cell('e', 14)
Cell('f', 15)
Cell('g', 16)
Cell('h', 17)
Cell('i', 18)
Cell('j', 19)
Cell('k', 20)
Cell('l', 21)
Cell('m', 22)
Cell('n', 23)
Cell('o', 24)
Cell('p', 25)
Cell('q', 26)
Cell('r', 27)
Cell('s', 28)
Cell('t', 29)
Cell('u', 30)
Cell('v', 31)
Cell('w', 32)
Cell('x', 33)
Cell('y', 34)
Cell('z', 35)
Cell('A', 36)
Cell('B', 37)
Cell('C', 38)
Cell('D', 39)
Cell('E', 40)
Cell('F', 41)
Cell('G', 42)
Cell('H', 43)
Cell('I', 44)
Cell('J', 45)
Cell('K', 46)
Cell('L', 47)
Cell('M', 48)
Cell('N', 49)

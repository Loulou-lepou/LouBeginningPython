
# Solve parametric quadratic equations
from math import sqrt
import sympy as sym


def quadratic_1(a, b, c):

    if a == 0:
        if b == 0:
            if c != 0:
                return print('no solutions')
            else:
                print('infinitely many solutions')
        else:
            print('unique solution', x, ' = ', - c / b)
    else:
        delta = b ** 2 - 4 * a * c
        print('\N{GREEK CAPITAL LETTER DELTA}', ' = ', delta)
        # print('\u0394 = ', delta)
        if delta < 0:
            print('no solutions')
        elif delta == 0:
            print('unique solution', x, ' = ', -  b / (2 * a))
        else:
            print('2 distinct real roots',
                  "x{}".format('\N{SUBSCRIPT ONE}'), ' = ', (- b - sqrt(delta)) / (2 * a),
                  ' ', 'x{}'.format('\N{SUBSCRIPT TWO}'), ' = ', (- b + sqrt(delta)) / (2 * a))


if __name__ == '__main__':

    a1 = int(input('a = '))
    b1 = int(input('b = '))
    c1 = int(input('c = '))

    # declare symbolic variable in SymPy to avoid error : unresolved reference 'x'
    x = sym.Symbol('x')
    print('We have the eqn',
          a1, x, '{}'.format('\N{SUPERSCRIPT TWO}'),
          '+', b1, x, '+', c1, ' = 0')

    quadratic_1(a1, b1, c1)

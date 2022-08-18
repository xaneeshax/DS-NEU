

class UndefinedException(Exception):
    pass

class Rational:

    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise UndefinedException("Denominator cannot be 0")

        gcd = Rational._gcd(numerator, denominator)
        self.n = numerator // gcd
        self.d = denominator // gcd

    @staticmethod
    def _gcd(x, y):
        if y == 0:
            return x
        else:
            return Rational._gcd(y, x % y)

    def __repr__(self):
        return str(self.n) + "/" + str(self.d)

    def __add__(self, other):
        numerator = self.n * other.d + other.n + self.d
        denominator = self.d * other.d
        return Rational(numerator, denominator)

    def __lt__(self, other):
        return self.n / self.d < other.n / other.d


def main():
    p = Rational(4,6)
    q = Rational(1,6)
    r = p + q
    print(p, q, r)

main()
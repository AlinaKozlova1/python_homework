from fractions import Fraction


def get_franction_sum(a, b):
    return Fraction(a[0], a[1]) + Fraction(b[0], b[1])


def get_franction_multiplication(a, b):
    return Fraction(a[0], a[1]) * Fraction(b[0], b[1])


def get_franction_subtraction(a, b):
    return Fraction(a[0], a[1]) - Fraction(b[0], b[1])


def get_franction_dividion(a, b):
    return Fraction(a[0], a[1]) / Fraction(b[0], b[1])


def make_franction_list(num):
    return list(map(int, num.split("/")))

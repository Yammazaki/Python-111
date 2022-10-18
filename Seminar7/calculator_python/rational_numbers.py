from fractions import Fraction as F


def rattional_operation(a: str, b: str, operator):
    r_a = F(a)   # fract_a
    r_b = F(b)   # fract_b
    return r_a+r_b if operator == '+' else r_a-r_b if operator == '-' \
        else float(round(r_a*r_b,3)) if operator == '*' else float(round(r_a/r_b,3)) if operator == '/' else False


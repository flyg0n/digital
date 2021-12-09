from schemdraw import Drawing, ImageFormat
from schemdraw.parsing.logic_parser import logicparse
import matplotlib
from sympy import symbols
from sympy.logic import SOPform

matplotlib.use("Agg")


def format(expression):
    return expression.replace("|", "+")


def solve(mssv):
    a, b, c, d = symbols("a b c d")
    predefined_minterm = [10, 11, 12, 14]
    predefined_dcare = [13, 15]
    x = [int(i) for i in list(mssv[4:])]
    x.reverse()
    minterm = []
    for p in x:
        if p in minterm:
            append_value = p
            while append_value in minterm:
                append_value += 1
                if append_value == 10:
                    append_value = 0
            minterm.append(append_value)
        else:
            minterm.append(p)
    print(f"x1: {minterm[0]}, x2: {minterm[1]}, x3: {minterm[2]}, x4: {minterm[3]}")
    predefined_minterm.extend([minterm[0], minterm[1], minterm[2]])
    predefined_dcare.append(minterm[3])
    predefined_minterm.sort()
    predefined_dcare.sort()
    print(f"F = m{predefined_minterm} + d{predefined_dcare}")
    result = SOPform([a, b, c, d], predefined_minterm, predefined_dcare)
    # circuit_drawer(result)
    return result


def circuit_drawer(expression):
    logicparse(expression, outlabel="F").save("test.png")


def main():
    # result = solve("20193076")
    # print(result)
    circuit_drawer("(a & b) | (a & c) | (b & c) | (~a & ~b & ~c & ~d)")


if __name__ == "__main__":
    main()

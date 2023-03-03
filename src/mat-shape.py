class DiagMatrix:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, b):
        return DiagMatrix([self.elements[i] + b.elements[i]
                           for i in range(0, len(self.elements))])

    def __mul__(self, b):
        return DiagMatrix([self.elements[i] * b.elements[i]
                           for i in range(0, len(self.elements))])

    def inv(self):
        return DiagMatrix([1.0 / self.elements[i]
                           for i in range(0, len(self.elements))])

    def __str__(self):
        return str(self.elements)

A = DiagMatrix([1, 2, 3])
B = DiagMatrix([1, 2, 3])

C = A + B
D = A * B
E = A.inv()
print(C)
#> [2, 4, 6]
print(D)
#> [1, 4, 9]
print(E)
#> [1, 0.5, 0.3333]


class UpperTrianglarMatrix:
    def __init__(self, rows):
        self.rows = rows

    def solve(self, b):
        X = []
        for row_idx, row in enumerate(self.rows):
            x = b[row_idx] / row[-1]
            for col_idx, coeff in enumerate(row[1:]):
                x -= coeff * X[col_idx]
            X.append(x)
        return X


U = UpperTrianglarMatrix([[1], [1, 2], [1, 2, 3]])
b = [2, 3, 4]
U.solve(b)
#> [1.0, 0.5, 0.3333333333333333]

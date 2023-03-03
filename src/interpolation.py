from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

A = Point(1, 1)
B = Point(2, 3)
C = Point(3, -1)

# A(1) = 1 ; A(2) = 0 ; A(3) = 0
P_A = lambda x: (x - B.x) * (x - C.x) / ((A.x - B.x) * (A.x - C.x))

# B(1) = 0 ; B(2) = 1 ; B(3) = 0
P_B = lambda x: (x - A.x) * (x - C.x) / ((B.x - A.x) * (B.x - C.x))

# C(1) = 0 ; C(2) = 0 ; C(3) = 1
P_C = lambda x: (x - A.x) * (x - B.x) / ((C.x - A.x) * (C.x - B.x))

# Polynôme de Lagrange
P_l = lambda x: P_A(x) * A.y + P_B(x) * B.y + P_C(x) * C.y


# Vérifions que les ordonnées correspondent bien avec celles attendues
print(f"P_l(A.x) : {P_l(A.x)}")
print(f"P_l(B.x) : {P_l(B.x)}")
print(f"P_l(C.x) : {P_l(C.x)}")
# $P_l(A.x) : 1.0$
# $P_l(B.x) : 3.0$
# $P_l(C.x) : -1.0$

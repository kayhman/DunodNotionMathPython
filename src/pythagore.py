import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def to_plot(self):
        return np.array([self.a, self.b, self.c])
a = 4
b = 3
c = 5
p0 = [0, 0]
p1 = [a, 0]
p2 = [a + b, 0]
p3 = [a + b, a]
p4 = [a + b, a + b]
p5 = [b, a + b]
p6 = [0, a + b]
p7 = [0, b]

p8 = [a, b]
p9 = [a, a + b]
p10 = [a + b, b]
p11 = [a, a + b]

points = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
T0 = Triangle(p0, p1, p7)
T1 = Triangle(p1, p2, p3)
T2 = Triangle(p3, p4, p5)
T3 = Triangle(p5, p6, p7)

triangles = [T0, T1, T2, T3]

plt.figure()
plt.scatter([p[0] for p in points], [p[1] for p in points])
for idx, triangle in enumerate(triangles):
    hatch = '/' if idx%2 else '\\'
    trg = plt.Polygon(triangle.to_plot(), hatch=hatch, fill=False)
    plt.gca().add_patch(trg)
plt.show()

T0 = Triangle(p0, p1, p7)
T1 = Triangle(p1, p8, p7)
T2 = Triangle(p10, p4, p8)
T3 = Triangle(p4, p11, p8)

triangles = [T0, T1, T2, T3]

plt.figure()
plt.scatter([p[0] for p in points], [p[1] for p in points])
for idx, triangle in enumerate(triangles):
    hatch = '/' if idx%2 else '\\'
    trg = plt.Polygon(triangle.to_plot(), hatch=hatch, fill=False)
    plt.gca().add_patch(trg)
plt.show()

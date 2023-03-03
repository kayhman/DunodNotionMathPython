import numpy as np
from mpmath import mp
from math import pi

mp.dps = 40 * 2

# Calcul de $\pi$ selon la formule
# de la surface d'un disque.
# $A = \pi r^2$
def pi_area(n):
    pi = mp.mpf(0.0)
    delta = mp.mpf(2.0/n)
    for x in np.linspace(-1, 1, n):
        pi += mp.sqrt(1-mp.mpf(x**2)) * delta
    return pi * 2

# Décompte du nombre
# de décimales correctes.
def correct_decimals(estimation):
    estr = str(estimation)
    pistr = str(mp.pi)
    count = 0
    while count < mp.dps and estr[count] == pistr[count]:
        count += 1
    return count

print(mp.pi)
#> 3.1415926535897932384626433832
#  795028841971693993751058209749
#  44592307816406286209
#> 15
print(pi_area(20))
print(correct_decimals(pi_area(20)))
#> 2.9464816642689353470203056254
#  826321581344348248804723822354
#  791484113951400421551
#> 0
print(pi_area(200))
print(correct_decimals(pi_area(200)))
#> \textbf{3}.1247061202031432619538905026
#  083467912687794382799556197738
#  748807729606833508025
#> 3
print(pi_area(2000))
print(correct_decimals(pi_area(2000)))
#> \textbf{3.1}399846612846459251816568252
#  812265456024177789488534798714
#  581757130788550688929
#> 3
print(pi_area(20000))
print(correct_decimals(pi_area(2000)))
#> \textbf{3.141}4343979492426024438839718
#  958882672172217043733174000354
#  706002355952922748001
#> 3
print(pi_area(200000))
print(correct_decimals(pi_area(20000)))
#> \textbf{3.1415}769084386255985120556707
#  854107347444745931828363984625
#  222130352877526667303
#> 5
print(pi_area(2000000))
print(correct_decimals(pi_area(200000)))
#> \textbf{3.14159}10816174841284496931527
#  730721488309631119895219492960
#  487870557535196434114
#> 6

# Calcul de $\pi$ selon la formule
# des frères Chudnovsky.
def pi_chudnowski(n):
    pi = mp.mpf(0.0)
    for k in range(0, n):
        num = (-1)**k * mp.factorial(6*k) * (13591409+mp.mpf(545140134)*k)
        den = mp.factorial(3*k) * mp.factorial(k)**3*mp.mpf(640320)**(3*k+3/2)
        pi += 12 * num / den
    return 1.0 / pi

print(pi_chudnowski(1))
print(correct_decimals(pi_chudnowski(1)))
#> \textbf{3.14159265358973}42076684535915
#  782983407622332609157065908941
#  454987376662094016591
#> 15
print(pi_chudnowski(2))
print(correct_decimals(pi_chudnowski(2)))
#> \textbf{3.1415926535897932384626433835}
#  873506884758663459963743156549
#  058068013014505652036
#> 28
print(pi_chudnowski(3))
print(correct_decimals(pi_chudnowski(3)))
#> \textbf{3.1415926535897932384626433832}
#  \textbf{7950288419716}76788548462879127
#  27790370642977335177
#> 43
print(pi_chudnowski(4))
print(correct_decimals(pi_chudnowski(4)))
#> \textbf{3.1415926535897932384626433832}
#  \textbf{795028841971693993751058209}849
#  474080206624527897174
#> 57
print(pi_chudnowski(5))
print(correct_decimals(pi_chudnowski(5)))
#> \textbf{3.1415926535897932384626433832}
#  \textbf{795028841971693993751058209749}
#  \textbf{44592307816}3466946903
#> 71
print(pi_chudnowski(6))
print(correct_decimals(pi_chudnowski(6)))
#> \textbf{3.1415926535897932384626433832}
#  \textbf{795028841971693993751058209749}
#  \textbf{44592307816406286209}
#> 80

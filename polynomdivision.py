"""POLYNOMDIVISION

Das Programm errechnet
den Polynomquotienten
mit Rest. Rechenschritte
werden ausgegeben.

NUTZUNG

Das Programm wird über
`F1` ausgeführt.
Eingegeben werden die
Koeffizienten in ana-
lytischer Anordnung
(a_n * x^n + ... + a_2 * x^2 + a_1 * x + a_0)
undnur durch ein Komma
getrennt.

Beispiel
--------

>>> Divident: 1,5,6
>>> Divisor:  1,2
[Ausgabe]
(1  5  6) : (1  2)
 1 2
    3 6
    3 6

Ergebnis:   [1, 3]
Rest:       [0]

Erstellt von Camillo Ballandt
15. September 2022.
"""

a = list(map(int, input("Divident: ").split(",")))
b = list(map(int, input("Divisor: ").split(",")))


def div(__x, __y):
    print("(", end="")
    print(*tuple(a), sep="  ", end="")
    print(") : (", end="")
    print(*tuple(b), sep="  ", end="")
    print(")")
    a_deg = len(__x)
    b_deg = len(__y)
    res = []
    rest = __y
    a_op = __x[0:b_deg]
    for i in range(a_deg - b_deg+1):
        digits = 0
        if i != 0:
            for ele in a[:i]:
                digits += len(str(ele))
            print(" " * (1 + 2*i + digits), end="")
            print(*tuple(a_op), sep=" ")
        if a_op[0] / __y[0] == a_op[0] // __y[0]:
            factor = a_op[0] // __y[0]
        else:
            factor = a_op[0] / __y[0]
        res.append(factor)
        b_op = [ele * factor for ele in b]
        print(" " * (1 + 2*i + digits), end="")
        print(*tuple(b_op), sep=" ")
        rest = [a_op[j] - __y[j] * factor for j in range(1, b_deg)]
        if i < a_deg - b_deg:
            a_op = rest + [__x[i + b_deg]]
    return res, rest


res, rest = div(a, b)
print("\nErgebnis:  ", res)
print("Rest:      ", rest)

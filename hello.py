from fractions import Fraction

f = Fraction(3, 4)
print(f + 2.5)

print(f + Fraction(1, 2) + 2)
print(f.numerator)

a = 2 + 3j
print(type(a))
print(a)
b = complex(2, 3)
print(b)

print(a + b)
print(a - 2 * b)

print(a.real)
print(a.imag)

print(a * b)

print(a.conjugate())

magnitude = (a.real ** 2 + a.imag ** 2) ** (1/2)
print(magnitude)
print(abs(a))


print(int('2'))
print(1.2.is_integer())
print(1.0.is_integer())




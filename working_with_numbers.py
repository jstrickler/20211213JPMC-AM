import math
# int float

i1 = 1000
i2 = 0b1000
i3 = 0x1000
i4 = 0o1000
print(i1, i2, i3, i4)
i5  = 2938508203985019385019835019835019385135135091835115391835018
print(i5 + 1)
i6 = 1_303_893
i7 = 13_03_89_3
print(i6, i7)

f1 = 123.456
f2 = 123.
f3 = .456
f4  = 1.0393e33

a = 25
b = 7
print()
print(a + b, a - b)
print(a * b, a / b, a // b, a // -b, math.ceil(a / b))
print(a ** b, a % b)

x = 5  #  x = int(5)
m = 13.3903
x = int(m)
print(x * 10)
a = "   123  "
print(int(a) + 2)

value = "12.3802"
print(value * 5)
print(float(value) * 5)





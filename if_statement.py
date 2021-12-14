value = 67
if value > 75:
    print("koala")
    print("kangaroo")
elif value > 50:
    print("wallaby")
    print("wombat")
    if value > 60:
        print("blue-ringed octopus")
else:
    print("quokka")
    print("platypus")

print("All done.")

name = "Bob"
if name:
    print("Bob bob bob")

# C/Java/etc
#  A ? B : C
# Python
#  B if A else C

debug = True
color = "red" if debug else "green"
print("color is", color)

#  == != > < >= <= is
a = 5
b = a
print(a is b)
c = 5
print(a is c)
print(id(a), id(b), id(c))















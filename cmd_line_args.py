import sys

print(sys.argv)
print("script name sys.argv[0]:", sys.argv[0])
print("first argument: sys.argv[1]:", sys.argv[1])
value = float(sys.argv[1])
print(value * 20)

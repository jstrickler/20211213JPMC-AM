import sys
# from pkg.pkg import module
from john.math import geometry

#  find and run geometry.py

c1 = geometry.circle_area(99)
print("c1: {}".format(c1))

r1 = geometry.rectangle_area(18, 32)
print("r1: {}".format(r1))

print(geometry.spam)

# module search order
#  1. current folder
#  2. folders in PYTHONPATH
#  3. folders in sys.prefix

for path in sys.path:
    print(path)






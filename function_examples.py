import math

def get_message():
    return "Hello, JPMC world"

m = get_message()
print("m: {}".format(m))
print(get_message())

def show_message():
    msg = get_message()
    print(msg)

x = show_message()
print(x)

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

print(circle_area(14))
ra = rectangle_area(8.5, 17)
print("ra: {}".format(ra))
diameter = 22
print(circle_area(diameter))

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass

wacky(1, 2, 3, 4, 5, 6, p5=18, p4=42, animal="wombat", country="Bukina Faso")

def count_lines(search_term, *file_paths, ignore_case=False):
    pass

count_lines('bird', 'DATA/alice.txt', 'DATA/parrot.txt', ignore_case=True)





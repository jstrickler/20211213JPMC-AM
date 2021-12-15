fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# naive approach
f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#     [   EXPR   for VAR in  ITERABLE if COND ...]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = [float(n * 2) for n in nums if n > 300]
print("n1: {}\n".format(n1))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print("dobs: {}\n".format(dobs))

SUITS = 'Clubs Diamonds Hearts Spades'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
cards = [(s, r) for s in SUITS for r in RANKS]
print("cards: {}\n".format(cards))

fruit_gen = (f.upper() for f in fruits if f.startswith('p'))
print(fruit_gen, type(fruit_gen))
print()
for fruit in fruit_gen:
    print(fruit)
print()


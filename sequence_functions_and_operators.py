a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("c: {}".format(c))

x = "foo"
y = "bar"
result = x + y
print("result: {}".format(result))  # FUBAR

print('-' * 60)
banner = "Python Rocks! " * 4
print("banner: {}".format(banner))

flags = [True] * 10
print("flags: {}".format(flags))
items = [None] * 3
print("items: {}".format(items))

actor = "Chris Hemsworth"
print("Hem" in actor)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print("'cherry' in fruits: {}".format('cherry' in fruits))
print("32 in nums: {}".format(32 in nums))
print("42 in nums: {}".format(42 in nums))

print("nums: {}".format(nums))
print(len(nums), min(nums), max(nums))
print(sorted(nums))
print()

print("fruits: {}".format(fruits))
print(len(fruits))
print(min(fruits), max(fruits), sorted(fruits))  # fruits.sort()
print()

print(sorted(actor))

print("fruits: {}\n".format(fruits))

rfruits = reversed(fruits)
print("rfruits: {}".format(rfruits))
for fruit in rfruits:
    print(fruit, end=' ')
print('\n')

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
e = enumerate(fruits)
print("first list:", list(e))
print("second list:", list(e))

print("partial loop I")
e = enumerate(fruits)
for i, fruit in e:
    print(i, fruit)
    if i == 13:
        break

print("partial loop II")
for i, fruit in e:
    print(i, fruit)

states = ['TX', 'NC', 'CA']
capitals = ['Austin', 'Raleigh', 'Sacramento']
sc = zip(states, capitals)
print("sc: {}".format(sc))
for state, capital in sc:
    print(state, capital)
print(list(zip(states, capitals)))
print('-' * 60)

r = range(1, 11)
print(r)
for i in r:
    print(i, end=",")
print("\n")
#  range(stop) range(start, stop)  range(start, stop, step)
for i in range(3):   # range of 0 through 4
    print("Hello, JPMC world")

i = 0
while i < 3:
    print("Hello, JPMC world")
    i += 1



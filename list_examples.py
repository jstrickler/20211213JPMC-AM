import sys

list1 = list()
list2 = [1, 2, 3]
list3 = []  # empty list
list4 = 'Clubs Diamonds Hearts Spades'.split()
print(list1, list2, list3, list4, '\n')
print(list4[0])

cities = ['Plano', 'Jersey City', 'Glasgow', 'Houston',
          'Tampa']
print(cities)
print(cities[0], len(cities))
cities.insert(0, 'Houston')
print(cities)
cities.insert(4, 'Durham')
print(cities)
cities.append('Columbus')
print(cities)
more_cities = ['Chicago', 'Seattle', 'San Diego']
cities.extend(more_cities)
print(cities)
cities.append(more_cities)
print(cities)
print(cities[11])
print(cities[11][1])
print(cities[11][1][4])

#  LIST.insert(0, VALUE) LIST.append(VALUE)  LIST.extend(ITERABLE)
del cities[11]
print("cities: {}".format(cities))
del cities[2]
print("cities: {}".format(cities))

cities.remove('Durham')
print("cities: {}".format(cities))

c = cities.pop()
print("c: {}".format(c))
print("cities: {}".format(cities))

print("cities.count('Houston'): {}".format(cities.count('Houston')))
print("cities.count('Miami'): {}".format(cities.count('Miami')))



c = cities.pop(2)
print("c: {}".format(c))
print("cities: {}".format(cities))

cities.remove('Houston')
print("cities: {}".format(cities))
# del LIST[pos] LIST.pop(pos=-1) LIST.remove(value)
print(cities[0], cities[3], cities[-1])
print(cities[len(cities)-1])
print("cities.index('Tampa'): {}".format(cities.index('Tampa')))
print("'Tampa' in cities: {}".format('Tampa' in cities))
print("cities: {}".format(cities))

# [start:stop]  [:stop]  [start:]
print("cities[0:3]: {}".format(cities[0:3]))
print("cities[:3]: {}".format(cities[:3]))
print("cities[1:5]: {}".format(cities[1:5]))
print("cities[-1]: {}".format(cities[-1]))
print("cities[-3:]: {}".format(cities[-3:]))

actor = 'Chris Hemsworth'
print("actor[:5]: {}".format(actor[:5]))
print("actor[6:9]: {}".format(actor[6:9]))
print("cities: {}".format(cities))
print()

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

s = "abc"
for char in s:
    print(char.upper())
print()

for arg in sys.argv[1:]:
    print("arg: {}".format(arg))















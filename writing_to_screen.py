person = "Cartman"
city = "South Park"
value = 11.3902398
print(person, city, value)
#  str(person) + ' ' + str(city) + ' ' + str(value) + '\n'
print("Done.")   # str("Done.") + '\n'
print(person, city, sep='/')
print(person, city, sep=", ")
print(person)
print(city)
print(person, end=' ')
print(city)

import sys
print(person, city, value)
sep = ' '
end = '\n'
sys.stdout.write(str(person) + sep + str(city) + sep + str(value) + end)

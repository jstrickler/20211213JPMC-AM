from datetime import date

person = 'Bill', 'Gates', 'Microsoft', date(1955, 10, 28)

print("person: {}".format(person))
print("person[0]: {}".format(person[0]))
print("person[-1]: {}".format(person[-1]))

print("len(person): {}".format(len(person)))

account_info = 'John', 'Doe', 12343.93, 'Cleveland', 10930

my_list = [1, 2, 3]
my_tuple = 1, 2, 3
my_other_tuple = 1,
my_other_other_tuple = ()
for t in my_tuple, my_other_tuple, my_other_other_tuple:
    print(len(t))

print(person[0], person[1])

first_name, last_name, product, dob = person  # iterable unpacking
print(first_name, last_name)

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

print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))

for person in people:
    print(person)
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name, dob)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

x, y, z = values[:3]
print(x, y, z)















from pprint import pprint

knight_data = {}  # empty dict

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()
print(knight_data['Arthur'][0])
print(knight_data['Robin'][1])
print()

for knight, data in knight_data.items():
    print(f"{data[0]:4s} {knight:8s} {data[2]}")
print()


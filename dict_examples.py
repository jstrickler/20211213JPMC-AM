d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 16, 'c': 7, 'r': 92}
d3 = {}  # empty dict
d2['z'] = 42
d2['m'] = 27
print("d2: {}".format(d2))
print("d2['r']: {}".format(d2['r']))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['RDU'])
print("len(airports): {}".format(len(airports)))
for code in 'RDU', 'LAX', 'BUR', 'EWR', 'WOMBAT':
    print(code, code in airports)
print()
print("airports['EWR']: {}".format(airports['EWR']))
# print("airports['CMH']: {}".format(airports['CMH']))
print("airports.get('RDU'): {}".format(airports.get('RDU')))
print("airports.get('CMH'): {}".format(airports.get('CMH')))
print("airports.get('CMH', 'Not found'): {}".format(airports.get('CMH', 'Not found')))
print("airports.setdefault('CMH', 'Columbus'): {}".format(airports.setdefault('CMH', 'Columbus')))
print("airports: {}".format(airports))

del airports['EWR']
print("airports: {}".format(airports))

print("airports.items:", airports.items())
# for key_var, value_var in DICT.items():
for code, name in airports.items():
    print(code, name)

letter_counts = {}
with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]
        if first_letter not in letter_counts:
            letter_counts[first_letter] = 0
        letter_counts[first_letter] = letter_counts[first_letter] + 1
        # letter_counts[first_letter] += 1
print("letter_counts: {}".format(letter_counts))






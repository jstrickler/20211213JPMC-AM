mary_countries = ['Burkina Faso', 'Japan', 'Uruguay', 'Nepal',
          'Italy', 'Botswana', 'Spain', 'Estonia', 'Germany', 'Canada']
sue_countries = ['Japan', 'Uruguay', 'Germany', 'Canada', 'Japan',
                 'Bolivia', 'Botswana', 'Japan', 'Australia',
                 'Nepal']

empty = set()
mary = set(mary_countries)
sue = set(sue_countries)
sue.add('Argentina')

print("Common:", mary & sue)  # intersection
print("Not common:", mary ^ sue)  # xor
print("All:", mary | sue)  # union
print("Only Mary:", mary - sue)
print("Only Sue:", sue - mary)

sue_list = list(sue)
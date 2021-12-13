actor = 'Chris Hemsworth'

print(actor)
print(actor.upper())
print(actor)
u = actor.upper()
print(u)
print(type(actor), len(actor))
print(actor.count('h'))
print(actor.lower().count('h'))
print('spam'.upper())
print(actor.startswith('Chris'), actor.startswith("Liam"))
print("Hem" in actor)
print("Haw" in actor)
print(actor.find('Chris'), actor.find('Liam'))
print(actor.find('worth'))
a = "abc"
b = "123"
c = "abc123"
print(a.isalpha(), a.isalnum(), a.isnumeric())
print(b.isalpha(), b.isalnum(), b.isnumeric())
print(c.isalpha(), c.isalnum(), c.isnumeric())

s = "      All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xxyyxxxxxxyyyyyyAll my exes live Texasxxxxyyyxyyyyyyyyyyyyyyyyyy"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()
raw_line = "spam\n"
line = raw_line.rstrip()

print(actor.replace('Chris', 'Liam'))

file_contents = 'one\ntwo\nthree'
print(file_contents.splitlines())

print(s)

s = "      All   my     exes   live in            Texas      "
print(s.split())

record = "one#two#three"
print(record.split('#'))





person = "Cartman"
city = "South Park"
value = 37.2393802

print(person, city, value)
print(person, "lives in", city)

print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}") # f-string

print("Value is {:.2f}".format(value))
print(f"Value is {value:.2f}")

big_number = 34850985203985203958
print("{:,d}".format(big_number))

x = 35
print(f">{x:05d}< >{x:5d}<")

print("%05d %5d" % (x, x))  # legacy





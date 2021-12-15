file_path = 'DATA/mary.txt'   #  DATA\mary.txt
#  C:\Users\student\Desktop\py3jpmcint4halfAM\DATA\mary.txt

mary_in = open(file_path)
# use file ...
mary_in.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove trailing \n
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

for start_letter in [chr(n) for n in range(97,123)]:
    count = 0
    output_file_name = f"{start_letter}_words.txt"
    with open('DATA/words.txt') as words_in:
        with open(output_file_name, "w") as words_out:
            for raw_line in words_in:
                if raw_line.startswith(start_letter):
                    count += 1
                    words_out.write(raw_line)
        print(f"{count} words started with {start_letter}")
print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.upper() + '\n')

# file modes
#  "r" -- read
#  "w" -- write/destroy
#  "a" -- write/append
#  "x" -- write unless exists

if True:
    pass

for i in range(5):
    pass

with open('DATA/mary.txt') as mary_in:
    pass







file_path = 'DATA/wombats.txt'
try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = [f.rstrip() for f in breakfast_in.readlines()]
    try:
        print(foods[25])
    except IndexError as err:
        print(err)

nums = [0, 800, 15, 80, 0, 1000, 32, "abc", 255, 400, 5, 5000]

for n in nums:
    try:
        result = 42 / n
    except ZeroDivisionError as err:
        print(err)
        # exit()
    except Exception as err:
        print("WOW WOW WOW", err)
    else:
        print(result)
    # finally:
    #     ....

print("All done")

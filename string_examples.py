w = "wombat"

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Python's a great language")
print('Python is a "great" language')
print("""Python's a "great" language""")
print("Python's a \"great\" language")
print('Python\'s a "great language')
#  print qq/Python's a "great" language\n/;
#  say qq/..../;

query = """
select *
from customer_account
where customer_name like 'smith%'
"""

print(len(s1), len(s2), len(s5))




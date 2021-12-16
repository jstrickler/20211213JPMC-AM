from carddeck import CardDeck
from jokerdeck import JokerDeck
d1 = CardDeck("Martha")
d2 = CardDeck("Jay")
d3 = CardDeck()
print(d1, d2)
# print(d1.get_dealer()) # getter
print(d1.dealer) # property
try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer.upper())

d1.shuffle()
print(d1.cards)
for _ in range(5):
    c = d1.draw()
    print(c)

d1.shuffle()
CardDeck.shuffle(d1)
CardDeck.shuffle(d2)
print('-' * 60)
j1 = JokerDeck("Albert")
j1.shuffle()
print(j1)
print(j1.cards)
print(len(j1), len(d1))
print(d1, d2)
from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _create_deck(self):  # "protected"
        super()._create_deck()  # find method in parent
        for num in '1', '2':
            card = Card(num, 'JOKER')
            self._cards.append(card)
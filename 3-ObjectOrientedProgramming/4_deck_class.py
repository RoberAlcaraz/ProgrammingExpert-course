import random


class Deck:

    suits = ['D', 'H', 'C', 'S']
    values = ['2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):

        deck = []
        for suit in Deck.suits:
            for value in Deck.values:
                deck.append(value + suit)
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, n_cards):

        if len(self.deck) < n_cards:
            return self.deck

        pop_cards = self.deck[len(self.deck)-n_cards:]
        self.deck = [card for card in self.deck if card not in pop_cards]
        return pop_cards

    def sort_by_suit(self):

        def my_order_func(strng):
            new_order = ['H', 'D', 'C', 'S']
            order = {key: i for i, key in enumerate(new_order)}
            if strng[1] == '0':
                return order[strng[2]]
            return order[strng[1]]

        self.deck.sort(key=lambda x: my_order_func(x))

    def contains(self, card):
        if card in self.deck:
            return True
        return False

    def __copy__(self):
        return type(self)()

    def copy(self):
        return self.__copy__()

    def get_cards(self):
        return self.deck[:]

    def __len__(self):
        return len(self.deck)


d = Deck()
deck1 = Deck()
for i in range(10):
    cards = deck1.deal(5)
    print(5, len(cards))
    print(len(deck1.get_cards()))
cards = deck1.deal(5)
print(2, len(cards))

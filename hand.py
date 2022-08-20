from card import Suit, Rank, Card
from collections import deque
from random import shuffle

class Set:
    def __init__(self, cards=[]):
        self.cards = deque(cards)

    def append_card(self, card):
        self.cards.append(card)

    def remove_card_by_index(self, index):
        if index >= len(self.cards):
            return None
        return self.cards.pop(index)

    def remove_card_by_value(self, target):
        if target in self.cards:
            index = self.cards.Index(target)
            return self.cards.pop(index)
        return False

    def sort_cards(self):
        self.cards.sort(key=lambda card: (card.suit, card.rank))
        return None

    def shuffle_cards(self):
        shuffle(self.cards)
        shuffle(self.cards)
        shuffle(self.cards)
        return None

class Hand(Set):
    def __init__(self, cards=[], player="Anonymous"):
        super().__init__(cards)
        self.player = player

class StandardDeck(Set):
    def __init__(self):
        super().__init__([])
        for suit in Suit.normal_suits:
            for rank in Rank.Numbers:
                self.append_card(Card(rank, suit))
            for rank in Rank.Faces:
                self.append_card(Card(rank, suit))
            self.append_card(Card(Rank.Ace, suit))
        for joker in range(2):
            self.append_card(Card(Rank.Joker, Suit.Joker))

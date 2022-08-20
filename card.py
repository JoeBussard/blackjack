from abc import ABC

class Suit:
    Hearts = 0
    Diamonds = 1
    Spades = 2
    Clubs = 3
    Joker = 4
    suit_name = ["Hearts","Diamonds","Spades","Clubs", "Joker"]
    normal_suits = [Hearts,Diamonds,Spades,Clubs,]

class Rank:
    Numbers = [2,3,4,5,6,7,8,9,10]
    Faces = ["Jack", "Queen", "King"]
    Ace = "Ace"
    Joker = "Joker"
    normal_ranks = [Numbers, Faces, Ace]


class Card(ABC):
    def __init__(self, rank=Rank.Ace, suit=Suit.Spades):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return str(self)

    def __str__(self):
        message = str(self.rank)
        if self.suit == Suit.Joker:
            return message
        message += " of " + Suit.suit_name[self.suit]
        return message

    def is_joker(self):
        return self.suit == Suit.Joker

    def color(self):
        if self.suit == Suit.Joker:
            return "joker"
        if self.suit == Suit.Hearts or self.suit == Suit.Diamonds:
            return "red"
        return "black"

    def __eq__(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

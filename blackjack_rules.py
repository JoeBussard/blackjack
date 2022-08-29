from card import Suit, Rank
import player as playerpy
import hand

class Blackjack:
    def __init__(self):
        self.TWENTYONE = 21
        self.players = []
        self.deck = hand.StandardDeck(hasJoker=False)

    def ace_low(self):
        if len(self.deck.cards != 52):
            return False
        for card in self.deck.cards:
            if card.rank == Rank.Ace:
                card.Rank = 1
        return True

    def add_player(self, player):
        self.players.append(player)

    def collect_cards(self):
        for player in self.players:
            for card in player.faceup.cards:
                self.deck.append_card(card)
                player.faceup.cards.remove_card_by_value(card)
            for card in player.facedown.cards:
                self.deck.append_card(card)
                player.facedown.cards.remove_card_by_value(card)
        print("now have", len(self.deck.cards))

    def set_up_game(self):
        self.dealer = playerpy.Table("Dealer")
        while len(self.players) < 1:
            print ("Add new player: ", end='')
            playername = str(input())[:10]
            new_player = playerpy.Player(playername)
            self.players.append(new_player)
        print("Ready to play.")

    def start_round(self):
        print("LET'S GET READY TO PLAY BLACKJACK!!")
        self.collect_cards()
        self.deck.shuffle_cards()

        print("Dealing first card.")
        for player in self.players:
            top_card = self.deck.remove_card_by_index(0)
            print("Dealt a", top_card, "to", player.name)
            player.faceup.append_card(top_card)

        top_card = self.deck.remove_card_by_index(0)
        print("Dealt a", top_card, "to the dealer")
        self.dealer.faceup.append_card(top_card)

        print("Dealing second card.")
        for player in self.players:
            player.faceup.append_card(self.deck.remove_card_by_index(0))
            print("Dealt a", top_card, "to", player.name)
        top_card = self.deck.remove_card_by_index(0)
        print("Dealt a face-down card to the dealer.")
        self.dealer.facedown.append_card(top_card)


#        self.dealer.facedown.append_card(self.deck.remove_card_by_index(0))

                #

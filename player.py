import hand

class Player:
    def __init__(self, name):
        self.name = name
        self.faceup = hand.Hand([])
        self.facedown = hand.Hand([])

    def say_faceup_cards(self):
        print("Face up,", self.name,"has")
        for card in self.faceup.cards:
            print(card)

    def say_facedown_cards(self):
        print("Face down,", self.name, "has")
        for card in self.facedown.cards:
            print(card)


class Table(Player):
    def __init__(self, name):
        super().__init__(name)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

class Robot(Player):
    def __init__(self, name):
        super().__init__(name)

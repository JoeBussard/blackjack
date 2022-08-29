import blackjack_rules
from blackjack_rules import Blackjack

mygame = Blackjack()

print(mygame)
mygame.collect_cards()

mygame.set_up_game()
mygame.start_round()

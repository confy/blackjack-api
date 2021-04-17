from datetime import datetime

class Hand:
    """ Defines one round of a hands, including player and dealer hand and other info """
    def __init__(self, hand_id, player_hand, dealer_hand, hand_pot, player_bal, date, result):
        self.id = hand_id
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.player_bal = player_bal
        self.hand_pot = hand_pot
        self.date = datetime.strptime(date, '%Y-%m-%d-%H:%M:%S')
        self.result = result
        
    def to_json(self):
        return {
            "id": self.id,
            "player_hand": self.player_hand,
            "dealer_hand": self.dealer_hand,
            "player_bal": self.player_bal,
            "hand_pot": self.hand_pot,
            "date": self.date.strftime('%Y-%m-%d-%H:%M:%S'),
            "result": self.result
        }
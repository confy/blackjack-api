import json

from .hand import Hand
from datetime import datetime

class HandManager:
    """ Manages hands """
    def __init__(self, filename:str, hands={}):
        self._filename = filename
        self._hands = hands
        self.add_json_file_to_hands()
    
    def add_json_file_to_hands(self):
        with open(self._filename, 'r') as f:
            hands_json_str = f.read()
            loaded_hands = json.loads(hands_json_str)
            
        for hand in loaded_hands:
            hand_id = hand["id"]
            loaded_hand = Hand(
                hand_id,
                hand["player_hand"], 
                hand["dealer_hand"],
                hand["hand_pot"], 
                hand["player_bal"],
                hand["date"],
                hand["result"],
                )
            self._hands[hand_id] = loaded_hand
        
    
    def get_hand_by_id(self, hand_id:int) -> Hand:
        if hand_id in self._hands:
            return self._hands[hand_id]
        return False
    
    def list_hands_for_web(self):
        """ Returns hands to display on web interface """
        return [hand.to_json() for hand in self._hands.values()]
    
    
    def get_hands(self) -> list:
        return self._hands.values()
    
    def add_hand(self, player_hand, dealer_hand, hand_pot, player_bal, date, result):
        """ Adds a new score """
        if len(self._hands.keys()) == 0:
            next_id = 1
        else:
            next_id = max(id for id in self._hands.keys()) + 1
        self._hands[next_id] = Hand(next_id, player_hand, dealer_hand, hand_pot, player_bal, date, result)
        
    def remove_hand_by_id(self, hand_id):
        if hand_id in self._hands.keys():
            self._hands.pop(hand_id)
            return True
        else:
            return False
        
    def save(self):
        """ Saves all the hands to the json file """
        all_hands_json = json.dumps([hand.to_json() for hand in self._hands.values()])
        with open(self._filename, 'w') as f:
            f.write(all_hands_json)
        
        
        
    
    
if __name__ == "__main__":
    hm = HandManager('hands.json')
    for hand in hm.get_hands():
        print(hand.to_json())
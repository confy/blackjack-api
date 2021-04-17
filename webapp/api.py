""" API Blueprint for the Blackjack hand API

defines routes:
/hands          - returns all hands in json
/hand/id        - returns a single hand with id - Accepts Post, Put, Get, or Delete
"""

from flask import Blueprint, jsonify, request

from models import HandManager

bp_api = Blueprint("api", __name__)


@bp_api.route("/hand/", methods=["POST"])
def create_hand():
    """ creates one hand and adds to the database """
    manager = HandManager('hands.json')
    data = request.get_json()
    
    manager.add_hand(data["player_hand"], data["dealer_hand"],
                      data["hand_pot"], data["player_bal"], data["date"], data["result"])
    manager.save()
    return "", 204
    
@bp_api.route("/hands")
def show_hands():
    """ Returns all hands in JSON format """
    manager = HandManager('hands.json')
    return jsonify([hand.to_json() for hand in manager.get_hands()])

@bp_api.route("/hand/<int:number>", methods=["GET"])
def show_hand(number):
    """ Shows one hand in json format """
    manager = HandManager('hands.json')
    hand = manager.get_hand_by_id(number)
    if not hand:
        return "hand not found", 404
    
    return jsonify(hand.to_json())

@bp_api.route("/hand/<int:number>", methods = ["DELETE"])
def remove_hand(number):
    manager = HandManager('hands.json')
    status = manager.remove_hand_by_id(number)
    if not status:
        return "Hand Not Found", 404
    else:
        manager.save()
        return "Hand Deleted", 204

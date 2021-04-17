from flask import Blueprint, render_template
from models import Hand, HandManager

bp_web = Blueprint("grades", __name__)

@bp_web.route('/')
def list_students():
    """ Index route for listing all students """
    manager = HandManager('hands.json')
    return render_template('index.html', hands=manager.list_hands_for_web())
    
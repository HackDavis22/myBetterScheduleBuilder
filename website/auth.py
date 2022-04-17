from flask import Blueprint, render_template
from logic import *

auth = Blueprint('auth',__name__)

@auth.route('selection', methods = ('GET', 'POST'))
def selection():

    return render_template("selection.html")
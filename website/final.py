from typing import final
from flask import Blueprint, render_template
from logic import *

final = Blueprint('final',__name__)

@final.route('res', methods = ('GET', 'POST'))
def res():
    return render_template("res.html")
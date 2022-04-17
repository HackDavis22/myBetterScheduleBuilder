from typing import final
from flask import Blueprint, render_template

final = Blueprint('final',__name__)

@final.route('res')
def res():
    return render_template("res.html")
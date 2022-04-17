from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('selection')
def selection():
    return render_template("selection.html")
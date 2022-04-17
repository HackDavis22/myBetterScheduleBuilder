from typing import final
from flask import Flask, url_for

from website.final import res

def create_app():
    app = Flask(__name__)

    app.config['SECRET KEY'] = 'BRUH'

    from .views import views
    from .auth import auth
    from .final import final

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    app.register_blueprint(final, url_prefix = '/')

    return app
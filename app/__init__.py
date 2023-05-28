from flask import Flask
from .controllers.sushi_controller import sushi_controller_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(sushi_controller_bp)
    return app

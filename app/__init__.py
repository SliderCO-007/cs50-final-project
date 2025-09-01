from flask import Flask
from .routes.main import main_blueprint
from .extensions import db

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main_blueprint)

    return app
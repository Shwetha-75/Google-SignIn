from flask import Flask 
from app.routes.routes import blue_print

def createApp():
    app=Flask(__name__)
    app.register_blueprint(blue_print)
    return app 

    
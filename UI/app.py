from flask import Flask
from Routes.home_routes import home
from Routes.start_FR_routes import StartFR
from Routes.register_routes import Register
from Routes.confirm_routes import Confirm
import tensorflow as tf

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(Register)
app.register_blueprint(StartFR)
app.register_blueprint(Confirm)
# Register other blueprints for different pages

if __name__ == '__main__':
    app.run()

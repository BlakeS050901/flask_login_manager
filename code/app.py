from flask import Flask
from config import Config
from routes import main
from extensions import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)




if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
from flask_migrate import Migrate

from dbs import create_app_db, create_redis_db
import config


app = Flask(__name__)
app.config.from_object(config)
db = create_app_db(app)

migrate = Migrate(app, db)

redis = create_redis_db(config.REDIS_DATABASE_URI)

from views import bp

app.register_blueprint(bp)


import models

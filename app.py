from flask import Flask
from example_blueprint import example_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(example_blueprint, url_prefix='/grammar')

from flask import Flask
from example_blueprint import example_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(example_blueprint, url_prefix='/grammar')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6699, ssl_context=('xiaomingya.com.pem', 'xiaomingya.com.key'))

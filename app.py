from flask import Flask
from example_blueprint import example_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(example_blueprint, url_prefix='/grammar')


@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小明呀</title>
</head>

<body>
    <p>Hello, 这里是小明的个人博客.
    </p>
    <p> 目前博客仍在建设中....</p>

</body>

</html>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6699)

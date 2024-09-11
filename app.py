from flask import Flask
from flask_cors import CORS

from example_blueprint import example_blueprint
from japanese_quiz_blueprint import japanese_quiz_blueprint
from japanese_word_blueprint import japanese_word_blueprint
from tool_blueprint import tool_blueprint

app = Flask(__name__)
CORS(app)

app.config["JSON_AS_ASCII"] = False
app.register_blueprint(example_blueprint, url_prefix="/grammar")
app.register_blueprint(tool_blueprint, url_prefix="/tool")
app.register_blueprint(japanese_word_blueprint, url_prefix="/word")
app.register_blueprint(japanese_quiz_blueprint, url_prefix="/quiz")


@app.route("/")
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
    <p> 建设中....</p>
</body>

</html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6699, debug=True)

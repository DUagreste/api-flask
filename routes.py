from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p> Ok! [Status Code: 200]</p>"


app.run()

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Ok! [Status Code: 200]"


app.run()

from flask import Flask

app = Flask(__name__)


@app.route("/healthcheck")
async def healthcheck():
    return "Ok! [Status Code: 200]"


app.run()

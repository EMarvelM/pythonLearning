#!/home/marvel/wurd/pythonLearning/Flask/web_flask/bin/python3
""" starts a flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


app.run()

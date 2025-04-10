from flask import Flask

app = Flask(__name__)

@app.route("/")
def return_csv():
    """Returns the CSV containing the test data"""
    return "Hello, world!"

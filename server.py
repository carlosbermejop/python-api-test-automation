from flask import Flask, send_file

app = Flask(__name__)

@app.route("/status")
def check_status():
    """Used to validate that the server is up before running the tests."""
    return "Server is running"

@app.route("/typeclass")
def return_csv():
    """Returns the CSV containing the test data."""
    return send_file("data/test-data.csv", as_attachment=True, download_name="data.csv")

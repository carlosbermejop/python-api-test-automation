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

@app.route("/json-1")
def return_json_1():
    return send_file("data/hugeJSON1.json",  as_attachment=True, download_name="json1.json")

@app.route("/json-2")
def return_json_2():
    return send_file("data/hugeJSON2.json",  as_attachment=True, download_name="json2.json")
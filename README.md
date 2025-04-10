# Python API Test Automation

This is a POC containing tests for the typeclass endpoint that returns a CSV containing information on whether a typeclass is an open or closed baumuster (oBM/gBM).

It downloads the CSV from the endpoints, validates the schema and verifies that if **typeclass_name** contains "FHS", "FHL", or "FHT", the **body_shape** should be gBM.

## Dependencies

It was developed using **Python 3.12.2** and uses the following packages:

- Flask==3.1.0
- pytest==8.3.5
- pytest-check==2.5.3
- pytest-html==4.1.1
- requests==2.32.3
- schema==0.7.7

They can be installed using the `requirements.txt` file included in the project. It is recommended to use a virtual environment for better control of the dependencies.

```cmd
python -m venv <path to the virtual environment (e.g. ./venv)>
./<path to the venv>/Scripts/activate
```
Install the dependencies by running the following command:
```
pip install -r requirements.txt
```

Exit the virtual environment by running:
```
deactivate
```

## Running the project

The project uses **Flask** to create a local server to replace the real endpoint from which to download the CSV — which in turn is kept in the `<root>/data/test-data.csv` file. To run the local server and the tests there are two options:

### Running the server and the tests independantly

To do this, open a terminal window, navigate to the root of the project and run the command `flask --app server run`

The following message will be printed to the screen:

```
* Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

If port 5000 is already busy in your machine, run the command as `flask --app server run --port <your port>`.

Keep this terminal window running for as long as you want to execute the tests.

To launch the tests, run the command `pytest .\src\tests\ --junitxml=.\output\xml\result.xml --html=.\output\report.html` from the root of the project.

Press Ctrl + C when you want to stop the server.

### Running the server and the tests simultaneously using a batch file

From the root of the project, run the command `.\start.bat` to use the batch file that will run the server and the tests simultaneously. Remember that the server won't be stopped automatically when the tests finish and you will have to press Ctrl + C to stop it.

## Reports

This POC includes generates two reports when the execution is finished:
- an XML file located at `<root>/output/xml/result.xml`;
- an HTML report located at `<root>/output/report.html`.

The XML report can be used for instance in a Jenkins CD/CI pipeline to validate a deployment.

The HTML provides an easier to understand glance at the stats for the test run and allows for specific data to be included to help in finding the root cause of issues.
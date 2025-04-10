start /b flask --app server run 
start /b pytest .\src\tests\ --junitxml=.\output\xml\result.xml --html=.\output\report.html
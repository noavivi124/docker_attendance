#!/usr/bin/python3

from flask import Flask
import attendance

app = Flask(__name__)

@app.route("/")
def dynamic_page():
	return attendance.main()


if __name__ == "__main__": 
	app.run(port="8000",debug = True)

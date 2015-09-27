from flask import Flask, request, render_template
from bot import Bot
import os

app = Flask(__name__)
b = Bot()

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/api/tell", methods=["POST"])
def tell():
	form = request.form
	response = "error connecting to the back end"
	if "statement" in form:
		stmt = form["statement"]
		response = b.tell(stmt)
	return response

port = int(os.getenv("VCAP_APP_PORT", "5000"))
host = os.getenv("VCAP_APP_HOST", "localhost")
app.run(port=port, host=host)


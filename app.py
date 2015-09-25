from flask import Flask, request, render_template
from bot import Bot

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

if __name__ == "__main__":
	app.run()


# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)


@app.route("/")
def index():
	# Just to test that the flask app + template are linked:
    hola = "Hello World!!!"
    # Sends the function result to the index.html template
    return render_template("index.html", x=hola)


# Leave as is
if __name__ == "__main__":
    app.run(debug=True)

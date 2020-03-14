# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)


@app.route("/")
def index():
    hola = "Hello World!!!"
    # Return the template with the list passed in
    return render_template("index.html", x=hola)


if __name__ == "__main__":
    app.run(debug=True)

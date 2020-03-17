# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import sqlalchemy as db

# Create an instance of our Flask app.
app = Flask(__name__)


# One wy of doing it
cnx = mysql.connector.connect(user='root', 
							  # add your mysql password here
							  password=<PASSWORD>, 
							  host='127.0.0.1', 
							  port = '3306',
							  database='bushfires_db')
cursor = cnx.cursor()


# Create an instance of our Flask app.
app = Flask(__name__)

@app.route("/")
def index():
	# Just to test that the flask app + template are linked:
    hola = "Hello World!!!"
    # Sends the function result to the index.html template
    return render_template("index.html", x=hola)


@app.route("/impact")
def impact():

	## One way of doing it

	#Makes the query
	query=("SELECT * FROM bushfires_db.protected_species_impact")
	cursor.execute(query)
	
	# Puts it all to a data frame
	sql_data = pd.DataFrame(cursor.fetchall())
	sql_data.columns = cursor.column_names

	# Closes the session
	cnx.close()

	# Shows the data as a table
	records = sql_data.to_html(index=False, header=True, classes="table")

	# Sends to template
	return render_template("impact.html", x=records)


# Leave as is
if __name__ == "__main__":
    app.run(debug=True)

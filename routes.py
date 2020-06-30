############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, session, request


################################### INIT APP ###################################


app = Flask(__name__)
app.secret_key = "stubblyainslieprocrastination"


################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('index.html',
						             session_username=session['username'] if 'username' in session else None)


################################ DIVISION & FEES ###############################


@app.route('/divisions-fees')
def divisions_fees():
	return render_template('divisions-fees.html')


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print(str(e))
	return """
		<h1 style="font-family:Avenir,'Nunito Sans';font-weight:lighter;">
			<strong>""" + request.path + """</strong> doesnt exist u moron.
		</h1>"""


#################################### APP RUN ###################################


if __name__ == "__main__":
    app.run(debug=True)

############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020 - July 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, session, request, Markup
from data import *
svg = {key: Markup(value) for key, value in svg.items()}


################################### INIT APP ###################################


app = Flask(__name__)
app.secret_key = "stubblyainslieprocrastination"


################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('index.html',
												 svg=svg,
						             session_username=session['username'] if 'username' in session else None)


################################ DIVISION & FEES ###############################


@app.route('/divisions-fees')
def divisions_fees():
	return render_template('divisions-fees.html',
												 divisionTableHeaders=divisionTableHeaders,
												 divisionTable=divisionTable,
												 challengerDescription=challengerDescription,
												 svg=svg)


################################### VOLUNTEER ##################################


@app.route('/volunteer')
def volunteer():
	return render_template('volunteer.html',
												 svg=svg)


################################### SCHEDULE ###################################


@app.route('/schedule')
def schedule():
	return render_template('schedule.html',
												 svg=svg)


################################### LOG IN ###################################


@app.route('/log-in')
def login():
	return render_template('log-in.html',
												 svg=svg)


#################################### SIGN UP ###################################


@app.route('/sign-up')
def sign_up():
	return render_template('sign-up.html',
												 svg=svg)


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print(e)
	return """
		<img src="https://image.freepik.com/free-vector/404-error-web-template-with-mad-cat_23-2147763345.jpg" align="left">
		<h1 style="font-family:Avenir,'Nunito Sans';font-weight:lighter;">
			<strong>""" + request.path + """</strong> doesnt exist u moron.
		</h1>
		<br><hr><br>
		<h2 style="font-family:Avenir,'Nunito Sans';font-weight:lighter;">
			if u think it should, put this in <b>routes.py</b>, <b>line 23</b> as a <b>temporary fix</b>
		</h2>
		<code><pre style="padding:20px;padding-right:30px;display:inline-block;background-color:#f1f1f1;">@app.route('""" + request.path + """')
def temporary():
	return render_template('"""+request.path[1:]+""".html',svg=svg)</pre>
		<code>"""


#################################### APP RUN ###################################


if __name__ == "__main__":
    app.run(debug=True)

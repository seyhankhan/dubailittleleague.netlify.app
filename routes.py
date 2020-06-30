############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, session, request, Markup
from vectors import svg
svg = {k: Markup(v) for k, v in svg.items()}


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
												 svg=svg)


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print(e)
	return """
		<h1 style="font-family:Avenir,'Nunito Sans';font-weight:lighter;">
			<strong>""" + request.path + """</strong> doesnt exist u moron.
		</h1>
		<img src="https://image.freepik.com/free-vector/404-error-web-template-with-mad-cat_23-2147763345.jpg">"""


#################################### APP RUN ###################################


if __name__ == "__main__":
    app.run(debug=True)

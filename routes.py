############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020 - July 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, request, session, Markup

from data import *
svg = {key: Markup(value) for key, value in svg.items()}


################################### INIT APP ###################################


app = Flask(__name__)
app.secret_key = "stubblyainslieprocrastination"


################################################################################
############################## REGISTRATION PAGES ##############################
################################################################################




############################## PLAYER REGISTRATION #############################


@app.route('/player-registration1')
def player_registration1():
	return render_template('player-reg1.html',
												 svg=svg)




################################################################################
############################### INFORMATION PAGES ##############################
################################################################################




################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('information-pages/index.html',
												 svg=svg,
						             session_username=session['username'] if 'username' in session else None)


################################ DIVISION & FEES ###############################


@app.route('/divisions-fees')
def divisions_fees():
	return render_template('information-pages/divisions-fees.html',
												 divisionTableHeaders=divisionTableHeaders,
												 divisionTable=divisionTable,
												 challengerDescription=challengerDescription,
												 svg=svg)


################################### VOLUNTEER ##################################


@app.route('/volunteer')
def volunteer():
	return render_template('information-pages/volunteer.html',
												 svg=svg)


################################### SCHEDULE ###################################


@app.route('/schedule')
def schedule():
	return render_template('information-pages/schedule.html',
												 svg=svg)




################################################################################
#################################### ERRORS ####################################
################################################################################




################################ MOBILE REDIRECT ###############################


@app.route('/error')
def error_page():
	return render_template('errors/error-mobile.html')


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print()
	print(e)
	print()
	return render_template('errors/error-404.html',
												 request_path=request.path)




################################################################################
#################################### APP RUN ###################################
################################################################################




if __name__ == "__main__":
    app.run(debug=True)

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




################################################################################
############################## REGISTRATION PAGES ##############################
################################################################################




##################################### LOGIN ####################################


@app.route('/login')
def login():
	return render_template('login.html',
												 svg=svg)



#################################### SIGNUP ####################################


@app.route('/signup')
def signup():
	return render_template('signup.html',
												 svg=svg)


################################# VERIFY EMAIL #################################


@app.route('/verify-email')
def verify_email():
	return render_template('verify-email.html',
												 svg=svg)


################################ FORGOT PASSWORD ###############################


@app.route('/forgot-password')
def forgot_password():
	return render_template('forgot-password.html',
												 svg=svg)


############################## PLAYER REGISTRATION #############################


@app.route('/player-registration1')
def player_registration1():
	return render_template('player-registration1.html',
												 svg=svg)

@app.route('/player-registration2')
def player_registration2():
	return render_template('player-registration2.html',
												 svg=svg)

@app.route('/player-registration3')
def player_registration3():
	return render_template('player-registration3.html',
												 svg=svg)

@app.route('/player-registration4')
def player_registration4():
	return render_template('player-registration4.html',
												 svg=svg)

@app.route('/player-registration5')
def player_registration5():
	return render_template('player-registration5.html',
												 svg=svg)

@app.route('/player-registration6')
def player_registration6():
	return render_template('player-registration6.html',
												 svg=svg)

@app.route('/player-registration-confirmation')
def player_registration_confirmation():
	return render_template('player-registration-confirmation.html',
												 svg=svg)

################################################################################
############################### INFORMATION PAGES ##############################
################################################################################




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




################################################################################
#################################### ERRORS ####################################
################################################################################


################################ MOBILE REDIRECT ###############################


@app.route('/error')
def error_page():
	return render_template('error-mobile.html')


################################# OTHER ROUTES #################################


@app.errorhandler(404)
def not_found(e):
	print()
	print(e)
	print()
	return render_template('error-404.html',
												 request_path=request.path)




################################################################################
#################################### APP RUN ###################################
################################################################################




if __name__ == "__main__":
    app.run(debug=True)

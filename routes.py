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


@app.route('/1')
def reg1():
	return render_template('registration/1-gender.html',
												 svg=svg)


@app.route('/2')
def reg2():
	return render_template('registration/2-dob.html',
												 svg=svg)


@app.route('/3')
def reg3():
	return render_template('registration/3-division.html',
												 svg=svg)


@app.route('/4')
def reg4():
	return render_template('registration/4-name-email.html',
												 svg=svg)


@app.route('/5')
def reg5():
	return render_template('registration/5-medical.html',
												 svg=svg)


@app.route('/6')
def reg6():
	return render_template('registration/6-id.html',
												 svg=svg)


@app.route('/7')
def reg7():
	return render_template('registration/7-parent.html',
												 svg=svg)


@app.route('/8')
def reg8():
	return render_template('registration/8-checkout.html',
												 svg=svg)


@app.route('/9')
def reg9():
	return render_template('registration/9-confirmation.html',
												 svg=svg)


################################################################################
############################### INFORMATION PAGES ##############################
################################################################################




################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('info-pages/index.html',
												 svg=svg,
						             session_username=session['username'] if 'username' in session else None)


################################ DIVISION & FEES ###############################


@app.route('/divisions-fees')
def divisions_fees():
	return render_template('info-pages/divisions-fees.html',
												 divisionTableHeaders=divisionTableHeaders,
												 divisionTable=divisionTable,
												 challengerDescription=challengerDescription,
												 svg=svg)


################################### VOLUNTEER ##################################


@app.route('/volunteer')
def volunteer():
	return render_template('info-pages/volunteer.html',
												 svg=svg)


################################### SCHEDULE ###################################


@app.route('/schedule')
def schedule():
	return render_template('info-pages/schedule.html',
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

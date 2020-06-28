############## Seyhan Van Khan & Alizeh Khan
############## Dubai Little League
############## June 2020
############## dubailittleleague.com

################################ IMPORT MODULES ################################


from flask import Flask, render_template, session


################################### INIT APP ###################################


app = Flask(__name__)
app.secret_key = "stubblyainslieprocrastination"


################################### HOME PAGE ##################################


@app.route('/')
def index():
	return render_template('index.html',
						             session_username=session['username'] if 'username' in session else None)


#################################### APP RUN ###################################


if __name__ == "__main__":
    app.run()

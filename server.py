""" Kid-O server"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Child, connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and debug toolbar

app.secret_key = "ABC"

# Raise error if there is an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined

#################
# INDEX & LOGIN #
#################

@app.route('/')
def index():
    """" Starting page with either login or personal profile if login session exists.
     For Log in: take email, password from user and check if credentials exist in the database
     by checking if email is in the users table. If email in table, redirect to the children overview.
     If not: redirect to sign up page."""

    if request.method == 'POST': # Process form if route gets POST request from /index
        email = request.form.get("email")
        password = request.form.get("password") #

        credentials = (email, password)

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Please sign up!')
            return redirect('/signup')
    else:
        if user.password != password:
            flash('Incorrect password.')
            return redirect('/')

        session['login_id']= credentials # Save session
        flash('You have sucessfully logged in.')
        return redirect("/overview.html") # Redirect to children's overview

    return render_template("index.html")

###########
# LOG OUT #
###########



###########
# SIGN UP #
###########

@app.route('/signup')
def signup_form():
    """ Sign up user """

    return render_template("signup.html")

#####################
# CHILDREN OVERVIEW #
#####################

@app.route('/overview')
def show_overview():
    """ Shows overview of all of the children in the project ordered by lastname."""

    all_children = db.session.query(Child).ordered_by(Child.child_last_name).all()

    return render_template('overview.html', all_children=all_children)


#################
# ADD NEW CHILD #
#################




######################
# EDIT CHILD PROFILE #
######################




########
# MAIN #
########

if __name__ == '__main__':

    # debug = True as DebugToolbarExtension is invoked

    app.debug = True
    connect_to_db(app)

    # User the DebugToolbar
    DebugToolbarExtension(app)

    app.run()

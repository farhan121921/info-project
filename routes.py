from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    request,
    url_for,
    session
)

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from app import create_app,db,login_manager,bcrypt
from models import User
from forms import login_form, otp_form,register_form
from flask_mail import Message
import random
from app import mail


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Home")

import random

# Function to generate a random 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)



@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.pwd, form.pwd.data):
            otp = generate_otp()  # Function to generate the OTP
            session['otp'] = otp
            session['email'] = user.email
            send_otp_email(user.email, otp)  # Send OTP to user's email
            flash("OTP sent to your email", "info")
            return redirect(url_for('verify_otp'))
        else:
            flash("Invalid username or password", "danger")

    return render_template("auth.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
    )

@app.route('/verify_otp/', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form.get('otp')  
        if entered_otp and str(session.get('otp')) == str(entered_otp):  
            user = User.query.filter_by(email=session['email']).first() 
            login_user(user)  
            flash("Login successful!", "success")
            session.pop('otp', None) 
            return redirect(url_for('index'))  
        else:
            flash("Invalid OTP!", "danger") 

    return render_template('verify_otp.html') 



def send_otp_email(email, otp):
    msg = Message('Your OTP Code', recipients=[email])
    msg.body = f"Your OTP code is {otp}. It will expire in 5 minutes."
    mail.send(msg)




# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data
            
            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )
    
            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")
    return render_template("auth.html",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account"
        )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)

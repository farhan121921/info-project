
# Final Project of Information Security

## Overview

This project implements a user authentication system using Flask, SQLAlchemy, and Flask-Login, featuring secure password storage with Bcrypt and an additional One-Time Password (OTP) verification step for enhanced security.

## Features

- **User Registration**: Users can create an account with a unique username and email address.
- **User Login**: Registered users can log in using their credentials.
- **OTP Verification**: Users receive an OTP via email for verification upon login.
- **Password Hashing**: Passwords are securely hashed using Bcrypt.
- **Session Management**: User sessions are managed with Flask-Login for easy authentication.
- **Database Management**: SQLite is used as the database to store user credentials.

## Technologies Used

- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: ORM for database interaction.
- **Flask-Bcrypt**: For hashing passwords.
- **Flask-Login**: For user session management.
- **Flask-WTF**: For handling forms securely.
- **SQLite**: Lightweight database for storing user information.
- **Email**: Used for sending OTPs to users.

## Installation

### Prerequisites

Make sure you have Python 3.6+ and pip installed on your machine.

### Clone the Repository

```bash
git clone https://github.com/yourusername/User-Authentication-in-Flask.git
cd User-Authentication-in-Flask
```

### Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Database Initialization

Before running the app, you need to create the database and tables:

```bash
# Initialize the database
flask db init
flask db migrate
flask db upgrade
```

## Configuration

Make sure to configure your email settings in the `app.py` file to enable OTP functionality. Replace the placeholders with your email credentials:

```python
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
```

## Running the Application

To run the application, use the following command:

```bash
flask run
```

You can now access the app at `http://127.0.0.1:5000`.

## Usage

1. **Register**: Navigate to `/register/` to create a new account.
2. **Login**: Go to `/login/` to log in with your credentials.
3. **OTP Verification**: After entering the correct credentials, check your email for an OTP. Enter the OTP on the verification page to complete the login process.

## Folder Structure

```
User-Authentication-in-Flask/
│
├── app.py
├── forms.py
├── manage.py
├── models.py
├── requirements.txt
├── routes.py
├── run
├── static/
│   ├── login.png
│   └── register.png
└── templates/
    ├── auth.html
    ├── base.html
    └── index.html
```

## Troubleshooting

- Ensure all dependencies are installed correctly.
- Check your email configuration settings for sending OTPs.
- If you encounter any issues, refer to the Flask documentation or check the console for error messages.


## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Flask-Bcrypt Documentation](https://flask-bcrypt.readthedocs.io/en/latest/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
```


# Flask Login Application

This is a Flask-based web application that provides user authentication functionality, including user signup, login, and account deletion. The application uses SQLAlchemy for database interactions and Werkzeug for password hashing.

## Features

- User Signup
- User Login
- Account Deletion
- Session Management with a 2-minute timeout

## Project Structure

```
flask_login/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── delete.py
│   │   ├── landing_page.py
│   │   ├── login.py
│   │   ├── signup.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── successfully_loggedin.html
│   ├── static/
│   │   ├── login_styles.css
│   │   ├── successfully_loggedin_styles.css
├── config.py
├── run.py
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask_login.git
   cd flask_login
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Ensure you have PostgreSQL installed and running.
   - Update the `SQLALCHEMY_DATABASE_URI` in `config.py` with your PostgreSQL credentials.

5. **Run the application:**
   ```bash
   python run.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Configuration

The application configuration is managed in `config.py`. Key configurations include:

- `SQLALCHEMY_DATABASE_URI`: Database connection URI.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Disable SQLAlchemy modification tracking.
- `SECRET_KEY`: Secret key for session management.

## Routes

### Signup

- **URL:** `/signup`
- **Methods:** `GET`, `POST`
- **Description:** Allows users to create a new account.

### Login

- **URL:** `/login`
- **Methods:** `GET`, `POST`
- **Description:** Allows users to log in to their account.

### Delete Account

- **URL:** `/login/delete`
- **Methods:** `POST`
- **Description:** Allows users to delete their account.

### Protected Route

- **URL:** `/protected`
- **Methods:** `GET`
- **Description:** A protected route that requires the user to be logged in.


## Flash Messages

Flash messages are used to provide feedback to the user. They are displayed in the `base.html` template and can be triggered in the routes using `flash()`.

## Models

### User

The `User` model represents a user in the application. It includes the following fields:

- `id`: Primary key.
- `username`: Unique username.
- `email`: Unique email address.
- `password`: Hashed password.
- `full_name`: Full name of the user.
- `created_at`: Timestamp of account creation.
- `dob`: Date of birth.
- `gender`: Gender.
- `mobile_number`: Unique mobile number.

## Templates

The application uses Jinja2 templates for rendering HTML pages. Key templates include:

- `base.html`: Base template that includes flash messages.
- `login.html`: Template for the login page.
- `signup.html`: Template for the signup page.
- `successfully_loggedin.html`: Template for the successfully logged-in page.

## Static Files

Static files such as CSS stylesheets are stored in the `static` directory.


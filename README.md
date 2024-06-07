## Flask Application Design

### Overview
The application is designed to create an account for a user if they don't have one. If they have an account, it authenticates them. The accounts are stored in Firebase Realtime Database. Each login is validated with a mobile phone two-factor authentication.

### HTML Files

- **index.html**: This is the home page of the application. It displays a simple login form with a username, password, and a submit button. There will be a link for creating an account if the user doesn't have one yet.
- **signup.html**: This page is for creating an account. It contains fields for the username, password, and phone number.
- **dashboard.html**: This page will display after successful login.

### Routes

- **@app.route('/')**: This route handles the home page by displaying **index.html**.
- **@app.route('/login', methods=['POST'])**: This route handles the login form submission by checking the credentials against the database and then performing phone number 2FA before redirecting to the dashboard.
- **@app.route('/signup', methods=['GET', 'POST'])**: This route handles user registration by creating an account in the database and then redirecting to the login page.
- **@app.route('/dashboard')**: This route is for the user dashboard. It is protected with login authentication and displays the user's information.
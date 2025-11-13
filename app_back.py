from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

# --- 1. CONFIGURATION AND INITIALIZATION ---
app = Flask(__name__)
# In a real app, you would configure a database here (e.g., app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db')

# --- Mock Database (For demonstration only - use a real database in production) ---
users = {} # {username: hashed_password} 

# --- 2. ROUTES AND LOGIC ---

@app.route('/')
def index():
    """Redirects to the registration page."""
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles the registration form submission."""
    if request.method == 'POST':
        # Get data from the form (using the 'name' attribute from HTML inputs)
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # --- Basic Validation ---
        if not username or not email or not password:
            return render_template('register.html', error="Please fill out all fields.")
        
        if username in users:
            return render_template('register.html', error="Username already exists. Try logging in.")
            
        # --- Security: Hashing the Password ---
        # NEVER store plain-text passwords!
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        
        # --- Mock Database Save ---
        users[username] = hashed_password
        print(f"New user registered: {username}, Email: {email}")

        # Redirect to a success page after successful registration
        return redirect(url_for('success'))
            
    # If it's a GET request, just render the empty form
    return render_template('register.html')

@app.route('/success')
def success():
    """Simple success confirmation page."""
    return render_template('success.html')


# --- 3. RUN THE APP ---
if __name__ == '__main__':
    # You must have 'register.html' and 'success.html' inside a folder named 'templates'
    print("--- Note: This is a Flask server setup. You need to run this file on your machine. ---")
    app.run(debug=True)

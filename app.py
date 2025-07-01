"""
PyPassword Generator - A secure web-based password generator
Built with Flask for customizable password generation
"""

from flask import Flask, render_template, request, jsonify, flash
import secrets
import string

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Secure secret key for sessions

# Character sets for password generation
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
ALL_LETTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS
NUMBERS = string.digits
SYMBOLS = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# Password generation constraints
MIN_CHARS = 0
MAX_CHARS = 50
MAX_TOTAL_LENGTH = 128


def validate_input(letters, symbols, numbers):
    """
    Validate user input for password generation
    
    Args:
        letters (int): Number of letters requested
        symbols (int): Number of symbols requested  
        numbers (int): Number of numbers requested
        
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        letters = int(letters)
        symbols = int(symbols)
        numbers = int(numbers)
    except (ValueError, TypeError):
        return False, "All inputs must be valid numbers"
    
    # Check individual constraints
    if not (MIN_CHARS <= letters <= MAX_CHARS):
        return False, f"Letters must be between {MIN_CHARS} and {MAX_CHARS}"
    
    if not (MIN_CHARS <= symbols <= MAX_CHARS):
        return False, f"Symbols must be between {MIN_CHARS} and {MAX_CHARS}"
    
    if not (MIN_CHARS <= numbers <= MAX_CHARS):
        return False, f"Numbers must be between {MIN_CHARS} and {MAX_CHARS}"
    
    # Check total length
    total_length = letters + symbols + numbers
    if total_length == 0:
        return False, "Password must contain at least one character"
    
    if total_length > MAX_TOTAL_LENGTH:
        return False, f"Total password length cannot exceed {MAX_TOTAL_LENGTH} characters"
    
    return True, ""


def generate_secure_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generate a cryptographically secure password
    
    Args:
        nr_letters (int): Number of letters to include
        nr_symbols (int): Number of symbols to include
        nr_numbers (int): Number of numbers to include
        
    Returns:
        str: Generated password
    """
    password_chars = []
    
    # Add letters (mix of uppercase and lowercase)
    for _ in range(nr_letters):
        password_chars.append(secrets.choice(ALL_LETTERS))
    
    # Add symbols
    for _ in range(nr_symbols):
        password_chars.append(secrets.choice(SYMBOLS))
    
    # Add numbers
    for _ in range(nr_numbers):
        password_chars.append(secrets.choice(NUMBERS))
    
    # Securely shuffle the password characters
    # Using secrets.SystemRandom for cryptographically secure shuffling
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_chars)
    
    return ''.join(password_chars)


@app.route('/')
def index():
    """Render the main password generator page"""
    return render_template('index.html')


@app.route('/generate_password', methods=['POST'])
def generate_password():
    """
    Handle password generation requests
    
    Returns:
        Rendered template with password or error message
    """
    try:
        # Get form data
        nr_letters = request.form.get('letters', '0')
        nr_symbols = request.form.get('symbols', '0')
        nr_numbers = request.form.get('numbers', '0')
        
        # Validate input
        is_valid, error_message = validate_input(nr_letters, nr_symbols, nr_numbers)
        
        if not is_valid:
            flash(error_message, 'error')
            return render_template('index.html', error=error_message)
        
        # Convert to integers (safe after validation)
        nr_letters = int(nr_letters)
        nr_symbols = int(nr_symbols)
        nr_numbers = int(nr_numbers)
        
        # Generate password
        password = generate_secure_password(nr_letters, nr_symbols, nr_numbers)
        
        # Calculate password strength
        strength = calculate_password_strength(nr_letters, nr_symbols, nr_numbers)
        
        return render_template('index.html', 
                             password=password, 
                             strength=strength,
                             letters=nr_letters,
                             symbols=nr_symbols,
                             numbers=nr_numbers)
        
    except Exception as e:
        # Log the error in production, for now just flash it
        error_msg = "An error occurred while generating the password. Please try again."
        flash(error_msg, 'error')
        return render_template('index.html', error=error_msg)


def calculate_password_strength(letters, symbols, numbers):
    """
    Calculate password strength based on composition
    
    Args:
        letters (int): Number of letters
        symbols (int): Number of symbols
        numbers (int): Number of numbers
        
    Returns:
        dict: Password strength information
    """
    total_length = letters + symbols + numbers
    
    # Basic strength calculation
    score = 0
    feedback = []
    
    # Length scoring
    if total_length >= 12:
        score += 25
    elif total_length >= 8:
        score += 15
    elif total_length >= 6:
        score += 5
    else:
        feedback.append("Consider using at least 6 characters")
    
    # Character variety scoring
    if letters > 0:
        score += 20
    else:
        feedback.append("Consider adding letters")
        
    if numbers > 0:
        score += 15
    else:
        feedback.append("Consider adding numbers")
        
    if symbols > 0:
        score += 25
    else:
        feedback.append("Consider adding symbols for better security")
    
    # Balanced composition bonus
    if letters > 0 and numbers > 0 and symbols > 0:
        score += 15
    
    # Determine strength level
    if score >= 80:
        level = "Very Strong"
        color = "#28a745"  # Green
    elif score >= 60:
        level = "Strong"
        color = "#ffc107"  # Yellow
    elif score >= 40:
        level = "Medium"
        color = "#fd7e14"  # Orange
    else:
        level = "Weak"
        color = "#dc3545"  # Red
    
    return {
        'score': min(score, 100),
        'level': level,
        'color': color,
        'feedback': feedback
    }


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('index.html', error="Page not found"), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    return render_template('index.html', error="Internal server error"), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

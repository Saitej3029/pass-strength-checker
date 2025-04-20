
from collections import Counter

def password_strength(password):
    # Initialize strength levels
    strength_levels = {
        'Very Weak': 0,
        'Weak': 1,
        'Moderate': 2,
        'Strong': 3,
        'Very Strong': 4
    }
    
    # Initialize score and feedback list
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    # Check for uppercase and lowercase characters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    # Check for special characters
    if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password):
        score += 1
    else:
        feedback.append("Add special characters like @, #, $, etc.")
    
    # Check for uniqueness (no more than 2 identical characters in a row)
    if not re.search(r"(.)\1\1", password):
        score += 1
    else:
        feedback.append("Avoid repeating the same character consecutively.")
    
    # Additional checks for improvement:
    # Check for common password patterns
    common_patterns = ['123456', 'password', 'qwerty', '111111', 'abc123']
    if any(pattern in password for pattern in common_patterns):
        feedback.append("Don't use common patterns like '123456', 'password', etc.")
    
    # Check for sequential characters
    if re.search(r"(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mn|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)", password.lower()):
        feedback.append("Avoid sequences like '123' or 'abc'.")
    
    # Check for keyboard patterns
    keyboard_patterns = ['qwerty', 'asdfgh', 'zxcvbn']
    if any(pattern in password.lower() for pattern in keyboard_patterns):
        feedback.append("Avoid keyboard patterns like 'qwerty'.")
    
    # Check for repeated characters
    if (Counter(password).most_common(1)[0][1] > 2):
        feedback.append("Don't repeat the same character too many times.")
    
    # Map score to strength level
    strength = [key for key, value in strength_levels.items() if value == score]
    
    # Return both strength and feedback
    return strength[0] if strength else 'Unknown', feedback

def estimate_crack_time(password):
    # Estimate based on password complexity and length
    # These are rough estimates and actual time may vary
    complexity = len(set(password))
    length = len(password)
    attempts_per_second = 1000000000  # 1 billion attempts per second for a powerful attacker
    
    # Calculate total combinations
    total_combinations = complexity ** length
    
    # Calculate time to crack in seconds
    time_to_crack = total_combinations / attempts_per_second
    
    # Convert time to a more readable format
    if time_to_crack < 60:
        return f"less than a minute"
    elif time_to_crack < 3600:
        return f"{time_to_crack // 60} minutes"
    elif time_to_crack < 86400:
        return f"{time_to_crack // 3600} hours"
    elif time_to_crack < 31536000:
        return f"{time_to_crack // 86400} days"
    else:
        return f"more than a year"

# Function to continuously check password strength
def continuous_password_check():
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to finish): ")
        if password.lower() == 'exit':
            print("Exiting password strength checker.")
            break
        strength, feedback = password_strength(password)
        crack_time = estimate_crack_time(password)
        print(f"Password: {password}")
        print(f"Strength: {strength}")
        print(f"Estimated time to crack: {crack_time}")
        if feedback:
            print("Feedback:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        print()  # Add a newline for better readability

# Example usage:
continuous_password_check()


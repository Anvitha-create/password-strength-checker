import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short": length_error,
        "No digit": digit_error,
        "No uppercase letter": uppercase_error,
        "No lowercase letter": lowercase_error,
        "No special character": symbol_error
    }

    if all(not e for e in errors.values()):
        return "Strong Password ✅"
    elif sum(errors.values()) <= 2:
        return "Moderate Password ⚠️"
    else:
        return "Weak Password ❌"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(check_password_strength(pwd))

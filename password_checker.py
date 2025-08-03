import string

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    symbol_error = not any(char in string.punctuation for char in password)

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        return "✅ Strong password!"
    else:
        print("❌ Weak password. Issues:")
        if length_error:
            print("- Must be at least 8 characters")
        if digit_error:
            print("- Must include at least one digit")
        if uppercase_error:
            print("- Must include at least one uppercase letter")
        if lowercase_error:
            print("- Must include at least one lowercase letter")
        if symbol_error:
            print("- Must include at least one special symbol")
        return ""

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password)
    if result:
        print(result)

# Task 5: Validate the user only when the username is admin and password is python123.
def validate_user(username, password):
    if username == "admin" and password == "python123":
        return "Valid"
    else:
        return "Invalid"


result = validate_user("admin", "python123")
print("User:", result)
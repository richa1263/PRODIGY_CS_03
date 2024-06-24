import re

def assess_password_strength(password):

    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@#$%^&+=]', password) is not None

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (@#$%^&+=).")


    if strength_score == 5:
        strength = "Strong"
    elif 3 <= strength_score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
for f in feedback:
    print(f"- {f}")

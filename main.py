import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) < 8:
        remarks = "😬 Too short! Make it at least 8 characters."
    else:
        if re.search(r"\d", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 1

        if strength == 1:
            remarks = "🟥 Very Weak – Add more variety!"
        elif strength == 2:
            remarks = "🟧 Weak – Getting there, but not safe."
        elif strength == 3:
            remarks = "🟨 Good – Almost strong!"
        elif strength == 4:
            remarks = "🟩 Excellent – Your password is super strong! 💪"

    print(f"\n🔍 Password Check Result:\n{remarks}\n")


print("🔐 Welcome to the Fun Password Strength Checker! 🚀")
print("Type your password to test it. Type 'exit' to quit.\n")

while True:
    user_input = input("💬 Enter password: ")
    if user_input.lower() == "exit":
        print("👋 Bye! Stay secure! 🛡️")
        break
    check_password_strength(user_input)

password = 123
attempt = input()
try:
    if(password==attempt):
        print("logged in successfully.")
except ValueError:
    print("Invalid password.")
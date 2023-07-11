#forgot password file
def forgot_password():
    try:
        username = input("Enter your username: ")

        with open('data/users.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == username:
                    print("Password recovery email sent to your registered email address.")
                    return

        print("Username not found. Please try again.")
    except Exception as e:
        print("Error occurred while recovering password:", str(e))

def staffLogin(user, psw):
    with open('staff.txt', 'r') as f:
        users = f.read()
        if user in users and psw in users:
            return user, psw
        else:
            return None

user = input("Input your username:")
psw = input("Input your pasword:")
print(staffLogin(user, psw))
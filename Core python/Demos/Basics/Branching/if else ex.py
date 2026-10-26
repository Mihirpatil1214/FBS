id = input('Enter Username = ')
pas = input('Enter password = ')

username = 'mihirpatil'
password = 'mihir123@'

if (username == id) and (password == pas):
    print('login successfull')
elif(username==id):
    print('password in incorrecoret.')
else:
    print('username is wrong.')
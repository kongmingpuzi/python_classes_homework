name=input('Please input the account name')
passwprd='8'*8
for i in range(3):
    if i==0:
        input_passwprd=input('Please input the account passwprd')
    else:
        input_passwprd=input('The wrong password!\nPlease input the account passwprd again.')
    if input_passwprd==passwprd:
        print('You have successfully logined in and have a good time in Python world.')
        break
    if i==2:
        print("You have inputted the wrong password three times and you can't input.")
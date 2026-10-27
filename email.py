# Email splitter
email = input('Email: ')

if('@'in email and email.index('@')-1 >= 0 and email.index('@')+1 < len(email)):
    # print(email.index('@'))
    print('Username:',email[:email.index('@')])
    print('Domain:',email[email.index('@')+1:])
else:
    print('Invalid email')

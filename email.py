# Email splitter
def email_split(email):
    name = ''
    mail = ''
    found = False
    for i in email:
        if(i == '@'):
            found = True
            continue
        if(found):
            mail+=i
        else:
            name+=i
    print('Username:',name)
    print('Domain:',mail)

email = input('Email: ')

if('@'in email and email.index('@')-1 >= 0 and email.index('@')+1 < len(email)):
    email_split(email)
    # print(email.index('@'))
else:
    print('Invalid email')

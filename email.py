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
email_split(email)
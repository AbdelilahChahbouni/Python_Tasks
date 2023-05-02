# Function That Tackes Email As Input And Return Username , Domain of The Email

def email_slicer():
    email = input("Enter PLease Your Email Like 'Exmple@gmail.com'  >> ")
    userName = email[:email.index("@") ]
    domaine = email[email.index("@") + 1:]
    print(userName , domaine)




email_slicer()




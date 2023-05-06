# Function That Tackes Email As Input And Return Username , Domain of The Email

def email_slicer():
    flag = True
    while flag:
        email = input("Enter PLease Your Email Like 'Exmple@gmail.com'  >> ")
        print(f"\nUserName >>> {email[:email.index('@')]} \nDomaine  >>> {email[email.index('@') + 1 :] }\n")
        anwser = input("You Want To Continue >>> Yes Or No ")
        if anwser == "no": flag = False



email_slicer()




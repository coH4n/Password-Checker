import string 
import optparse
def check_password(password):
    
    if len(password) < 8:
        return False

    with open("wordlist.txt","r") as f:
        wordlist = f.read().splitlines()
    
    if password in wordlist:
        return  False
    
    password_lower = any(str(char.islower() for char in password))
    password_upper = any(str(char.isupper() for char in password))
    password_isdigit = any(str(char.isdigit() for char in password))
    password_special = any(str(char.punctutation for char in password))

    if not(password_lower and password_upper and password_special and password_isdigit):
        return False
    
    return True

def get_user_input():
    parse = optparse.OptionParser()
    parse.add_option("-p","--password",dest="password",help="enter password")
    args = parse.parse_args()

    (user_inputs,arguments) = args 

    if check_password(user_inputs.password) == True:
        print("Password is strong")
    else:
        print("Password is weak")

get_user_input()
    

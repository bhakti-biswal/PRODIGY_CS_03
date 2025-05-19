import math
import string

def entropy_check(password):
    size=0
    if any(i in string.digits for i in password):
        size+=10
    if any(i in string.ascii_uppercase for i in password):
        size+=26
    if any(i in string.ascii_lowercase for i in password):
        size+=26
    if any(i in string.whitespace for i in password):
        size+=6 
    if any(i in string.punctuation for i in password):
        size+=32
    if size == 0:
        return 0
    entropy = len(password) * math.log2(size)
    return entropy
def main():
    strength=0
    password=input("Enter password:")
    entropy=entropy_check(password)
    if len(password)>=8:
        strength+=1
    if len(password)>=16:
        strength+=1
    if strength==2 :
        if entropy<40:
            print("Weak Password")
        elif entropy<60:
            print("Moderate Password")
        elif entropy<80:
            print("Strong Password")
        else:
            print("Excellent Password")
    else:
        print("Weak Password")

if __name__=="__main__":
    main()





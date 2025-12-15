import random
import string
print("\n Smart Password Creator")
length = int(input("How long should the password be? "))
source = string.ascii_letters + string.digits + "!@#$%^&*()?"
password = "".join(random.choice(source) for _ in range(length))
print(f" Your Secure Password: {password}")
print(" Save it somewhere safe!")
                   

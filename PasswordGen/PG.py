import random
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = ",;:.-_!*?/+#%~"
upper = True
lower = True
nums = True
syms = True

all = ""
# Checks what is allowed
if upper:
    all +=uppercase_letters

if lower:
    all+=lowercase_letters

if nums:
    all+= numbers
if syms:
    all+= symbols


# This dictates how long the password will be. 
length= 9
amount= 1

#Prints password
for x in range(amount):
    password= "".join(random.sample(all, length))
    print (password)


#Saves Used Passwords
with open('PasswordGen/%Previously Used.txt', 'wt') as f:
    print ("This will be replaced if program is ran again so make sure you make a backup of these passwords :D :"+password,file=f)
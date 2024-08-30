#Password Generator
#Importing modules
import string
import random

#Prompting the letters,digits and special characters
s1 = string.ascii_letters   #A-Z and a-z
s2 = string.punctuation     #spcl char @,!,etc
s3 = string.digits           #0-9

#Making the empty list and extending the characters in it
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
random.shuffle(s)       #shuffle function is used for list

P = int(input("Enter the number of characters you need: "))
print("".join(s[0:P]))
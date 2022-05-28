import re

string="aabbbbba"

c = re.search("bbbbb.*a$", string)

if c:
  print("correct")
else:
  print("wrong")

def q0(i):
    if i<len(string) and string[i]=='a':
         result=q0(i+1)
         if result==True:
            return True

    if i<len(string) and string[i]=='b':
        result=q1(i+1)
        if result==True:
            return True
        
    return False

def q1(i):
    if i<len(string) and string[i]=='a':
         result=q1(i+1)
         if result==True:
            return True

    if i<len(string) and string[i]=='b':
        result=q2(i+1)
        if result==True:
            return True

    return False

def q2(i):
    if i<len(string) and string[i]=='a':
         result=q2(i+1)
         if result==True:
            return True

    if i<len(string) and string[i]=='b':
        result=q3(i+1)
        if result==True:
            return True

    return False

def q3(i):
    if i<len(string) and string[i]=='a':
         result=q3(i+1)
         if result==True:
            return True
        
    if i<len(string) and string[i]=='b':
        result=q4(i+1)
        if result==True:
            return True

    return False

def q4(i):
    if i<len(string) and string[i]=='a':
        result=q4(i+1)
        if result==True:
            return True
        
    if i<len(string) and string[i]=='b':
        result=q5(i+1)
        if result==True:
            return True

    return False

def q5(i):
    if i<len(string) and string[i]=='a':
        result=q5(i+1)
        if result==True:
            return True

    if i<len(string) and string[i]=='b':
        result=q5(i+1)
        if result==True:
            return True

    if i<len(string) and string[i]=='a':
        result=q6(i+1)
        if result==True:
            return True




    return False

def q6(i):
    if i==len(string):
        return True
    else:
        return False


result=q0(0)
print(result)


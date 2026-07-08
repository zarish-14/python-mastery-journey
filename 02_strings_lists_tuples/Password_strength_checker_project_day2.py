print("===============================================================")
print("=====------=========PASSWORD STRENGTH CHECKER========------=====")
print("===============================================================")
password=input("Enter your password please= ") #input password
len_of_password=len(password) #use len function for length
print("Password Analysis")
if (len_of_password>=8):
    print("Length             :Good")
else:
    print("Length             :Bad")
has_digit=False
has_upper=False
has_lower=False
has_special=False
for ch in password: # for loop
    if ch.isupper():
        has_upper=True
    elif ch.islower():
         has_lower=True
    elif ch.isdigit():
         has_digit=True
    else:
         has_special=True
if has_upper:
    print("Uppercase Letter  : Yes")
else:
    print("Uppercase Letter  : No")

if has_lower:
    print("Lowercase Letter  : Yes")
else:
    print("Lowercase Letter  : No")

if has_digit:
    print("Digit             : Yes")
else:
    print("Digit             : No")

if has_special:
    print("Special Character : Yes")
else:
    print("Special Character : No")
#rules:
if len_of_password<8 or ((not has_digit) and (not has_special)): 
    result="Weak"
elif has_digit  and has_upper and has_lower and has_special:
     result="Strong"
elif (has_lower or has_upper) and has_digit:
    result="Medium"
else:
    result="Weak"
print("Result             :",result) 
if result == "Weak":
    print("Suggestions:")
    if len_of_password<8:
        print("Too short")
    if not has_digit:
        print("Add at least one digit")
    if not has_lower:
        print("Add at least one lower case letter")
    if not has_upper:
        print("Add at least one upper case letter")
    if not has_special:
        print("Add at least one special character (@,#,$ etc)")
if result == "Medium":
    print("Suggestions:")
    if not has_special:
        print("Add at least one special character (@,#,$ etc)")
    if not has_lower:
        print("Add at least one lower case letter")
    if not has_upper:
        print("Add at least one upper case letter")
    
print("Thank You!")

       
       
     
     
          


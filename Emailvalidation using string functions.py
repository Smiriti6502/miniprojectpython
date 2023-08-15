email=input("enter your email:" )#g@g.in, cube@gmail.com
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                    
                if k==1 or j==1 or d==1:
                    print("wrong email 5 - should not have a space and capital letter")
                else:
                    print("correct email")
            else:
                print("wrong email 4 - dot in the wrong position")
        else:
            print("wrong email 3 - @ should be used once")
    else:
        print("wrong email 2 - first letter must be an alphabet")
else:
    print("Wrong email 1 - length should be min 6")


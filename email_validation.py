email = input("Enter your Email: ")

if len(email) >= 6 : #checkinh if length is less than 6
    if email[0].isalpha(): #if first letter not alpha
        if ("@" in email) and (email.count("@") == 1): #if @ is there and only one is there. using XOR
            if (email[-4] == ".") ^ (email[-3] == "."): #if . is there in 3rd last or 4th last position
                flag = True
                for i in email:
                    if i==i.isspace(): #if any space is there
                        flag = False
                    elif i.isalpha():
                        if i ==i.upper(): #if any upper case is there
                            flag = False
                    elif i.isdigit():   #if any digit then no issue . pass
                        continue
                    elif i =="_" or i =="." or i =="@": #if(_/./@) then pass
                        continue
                    else:   #any other character then flag = False
                        flag = False
                if flag == True:    #if flag remains True after checking above condition then it's a right email
                    print("right email")
                else:
                    print("wrong email 5")
            else:
                print("wrong email 4") 
        else:
           print("wrong email 3") 
    else:
        print("wrong email 2")
else:
    print("wrong email 1 ")

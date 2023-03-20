age=input("how old are you :")
sex=input(" SEX :")
Age=int(age) 
if Age < 18 and sex=="male":
    print("you can't join...")
    print("you're a boy...")
if Age < 18 and sex=="female":
    print("you can't join...")
    print("you're a girl....")
elif Age > 18 and sex=="male":
    print("welcome to EDM II........")
    print("you're ma man ..")
elif Age > 18 and sex=="female":
    print("Welcome o sml ...")
    print("you're ma lovely girl..")

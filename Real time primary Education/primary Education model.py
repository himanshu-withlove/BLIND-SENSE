from pickle import TRUE
import myfunc2

while TRUE:   
    val=input("Enter the Text :")
    te=val
    if val=="exit":
        exit()
    else:
        te=val
        myfunc2.newfunc2(te)
        

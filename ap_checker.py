#if the second value is equal to the difference of first value from the zeorth value progression is an arithmetic one
def ap_check():
    prog_val = list(input("please enter numbers: ")) 
    d =  prog_val[1] - prog_val[0]
    if prog_val[2] == d + prog_val[1]:
        print("progression is arithmetic")
    else:
        print(" this is not an arithmetic progresion")
    
ap_check()
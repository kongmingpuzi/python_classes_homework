#https://zhuanlan.zhihu.com/p/387372009
def input_():
    length=input("Please input the length whose unit is cm or m ")
    return length
def cm2m(length_cm):
    return 0.01*float(length_cm)
def m2cm(length_m):
    return 100*float(length_m)
def judge_print(length):
    try:
        if(length[-2:]=='cm'):
            print("The length is "+str(cm2m(length[:-2]))+"m.")
        elif(length[-1]=='m'):
            print("The length is "+str(m2cm(length[:-1]))+"cm.")
        else:
            print("The input of unit error")
    except:
        print("The input of number error")
length=input_()
judge_print(length)
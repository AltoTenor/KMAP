
from Changing_Input_To_Indexes import citi
from solve4 import solve4

#DRIVER CODE

def kmap4(oc):
    a=input("Enter the variable names.\nFirst: ")
    b=input("Second: ")
    c=input("Third: ")
    d=input("Fourth: ")
    if oc==1:
        exp=input("Enter the expression (Eg:a'b'c'd+abc'd with no spaces) : ")
        finalans=(solve4(citi(exp,a,b,c,d)))
        
    else:
        exp=list(map(int,input("Enter the indexes seperated by spaces: ").split()))
        finalans=(solve4(exp))

    for i in range(len(finalans)-1):
        if finalans[i]=='a':
            print(a,end='')
        elif finalans[i]=='b':
            print(b,end='')
        elif finalans[i]=='c':
            print(c,end='')
        elif finalans[i]=='d':
            print(d,end='')
        elif finalans[i]=='+':
            print('+ ',end="")
        else:
            print(finalans[i],end='')

kmap_size=int(input("How many variables does your expression have? (2/3/4)\n"))
while True:
    option_choice=int(input("Enter how you want to input the terms\n 1.Sum of Minterms\n 2.Indexes of Minterms\n"))
    if option_choice in (1,2):
        break
    else:
        print("Inavlid Choice. ")

if kmap_size==4:
    kmap4(option_choice)
elif kmap_size==3:
    print("ONLY size 4 available for now")
#     kmap3(option_choice)
elif kmap_size==2:
    print("ONLY size 4 available for now")
#     kmap2(option_choice)
else:
    print("Out of scope. ")
n=int(input("please enter a number: "))
i=0
j=1
t=0

if n==1:
    print(0)
elif n>1:
    print(0)
    print(1)
    k=2
    while k<n:
        t=i+j
        i=j
        j=t
        print(t)
        k+=1
    

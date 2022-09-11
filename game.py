a=int(input("Enter the number to guess : "))
t=0
p=1
g=81
while(p):
    if(g==a):
        p=0
    elif(g<a):
        p=1
        print("Oh! You entered greater  number")
        a=int(input("Enter again any number to guess: "))
        t=t+1
    elif(g>a):
        p=1
        print("Oh! You entered  lower  number")
        a=int(input("Enter again any number to guess : "))
        t=t+1
    if(p==1):
        print("Sorry ! Try next time")
        a=int(input("Enter again any number to guess : "))
        t=t+1
        
print("Congrates ! You win the game")
print("You have tried : ",t+1," times")
        
        

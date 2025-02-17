#Game devleopment
#General Knowledge Quiz
def Game1():
    marks=0
    print("Name the folk dance of Andhra Pradesh?")
    print("Choose your options:\n1.Bollywood\n2.Hiphop\n3.Jazz\n4.Kuchipuddi")
    a=eval(input("Enter option :"))
    if a==4:
        marks=marks+4
        print("Correct ans")
    else:
        print("Wrong")
        marks=marks
    print("Name the largest river in the world?")
    print("Choose your options:\n1.Amazon\n2.Yamuna\n3.Ganga\n4.Godavri")
    a=eval(input("Enter option :"))
    if a==1:
        marks=marks+4
        print("Correct ans")
    else:
        print("Wrong")
        marks=marks
    print("In which month is Environment day is celebrated?")
    print("Choose your options:\n1.Jan\n2.June\n3.April\n4.March")
    a=eval(input("Enter option :"))
    if a==2:
        marks=marks+4
        print("Correct ans")
    else:
        print("Wrong")
        marks=marks
    print("Where is Gir National Park located?")
    print("Choose your options:\n1.Haryana\n2.Gujrat\n3.Maharastra\n4.Punjab")
    a=eval(input("Enter option :"))
    if a==2:
        marks=marks+4
        print("Correct ans")
    else:
        print("Wrong")
        marks=marks
    print("Your Total Score",marks)    
#Game1()

#Random no generation
def Game2():
    import random
    a=random.randint(0,9)
    un=eval(input("Enter your number :"))
    if a==un:
        print("System generated number :",a)
        print("Hurray!!! You are the winner")
    else:
        print("System generated number :",a)
        print("Better luck next time")
#Game2()

#Bidding amount depends on computer generated number and cash prize won amount depends on the condition
def Game3():
    import random
    n=random.randint(2,12)
    Amt=eval(input("Enter the amount you want to bid :")) 
    print("Computer Generated number :",n)
    if n==7:
        Amt=Amt*10
        print("Hurrah you are the winner",Amt)
    elif n<7:
        Amt=Amt-(Amt*0.25)
        print("Your Final Amt",Amt)
    elif n>7:
        Amt=Amt-(Amt*0.15)
        print("Your Final Amt",Amt)
#Game3()

#Stone-Paper-Scissor
def Game4():
    import random
    l=['stone','paper','scissor']
    a=input("Your turn :")
    n=random.choice(l)
    if a==n:
        print("Its a Tie")
        n=random.choice(l)
        a=print("Please choose from stone/paper/scissor")
        print(n)
    elif a=='paper' and n=='stone' or a=='scissor' and n=='paper' or a=='stone' and n=='scissor':
        print("Hurray you are the winner!")
    else:
        print("Opps! Bad Luck")
#Game4()

def Game5():
    import random
    a=random.randint(0,6)
    b=eval(input("Enter Number:"))
    print("Computer generated number",a)
    if a==b:
        print("Try again")
    elif b>a:
        print("You won")
    elif b<a:
        print("Computer won")
#Game5()

def Game6():
    import random
    a=random.randint(0,9)
    b=eval(input("Enter bid amt:"))
    for i in range(0,3):
        un=eval(input("Enter your number :"))
        if a==un:
            print("You are the winner")
            b=b+b*10
        else:
            print("You lose")
            b=b-(b*0.20)
    print("Computer generated number :",a)
    print("Final wallet amt",b)
#Game6()
        

        
        
        
                 

        
        


        
            
            
             
        
        
            
            
    
    
        



        

    
    
    
    
   





        


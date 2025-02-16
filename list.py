def Q1():
    #Print Hello World
    print("Hello World !")
Q1()

def Q2():
    #sum of two numbers
    s=0
    l= eval(input("Enter Numbers :"))
    for i in l:
        s= s+ i
    print("Sum of two number", s)
Q2()

def Q3():
    #Max from the list
    m=0
    l= eval(input("Numbers :"))
    for i in l:
        if i>m:
            m=i
    print("Max number from the list :", m)
Q3()

def Q4():
    #Sum of all elements
    s=0
    l=eval(input("Enter List :"))
    for i in l:
        s= s + i
    print("Sum of all elements",s)
Q4()

def Q5():
    a=0
    b=1
    c=0
    n=eval(input("Enter N : "))
    print(a," ",b,"",end=" ")
    #Print Fibonacci numbers
    while c<=n:
        c= a + b
        print(c,end="  ")
        a=b
        b=c
Q5()

def Q6():
    #check whether the number is prime or not
    x= eval(input("Enter No :"))
    y= 0
    for i in range(2,x):
        if x%i==0:
            y=1

        if y==1:
            print(x,"Is not prime number")
        elif y==0:
            print(x, "Is a prime number")
        else:
            print("Error")
Q6()

def Q7():
    #reverse a string
    s=input("Enter Word :")
    print(s[::-1])
Q7()
        
def Q8():
    #count the vowels
    v=0
    ch=input("Enter Word:")
    for i in ch:
        if i in 'aeiouAEIOU':
            v+=1
    print("Num of vowel",v)
Q8()

def Q9():
    #palindrome or not
    x= input("Enter word :")
    y=x[::-1]
    if x==y:
        print('palindrome')
    else:
        print('Not')
#Q9()

def Q10():
    #Ascending order
    l= eval(input("Enter NO :"))
    print(sorted(l))
Q10()

def Q11():
    #sum of elements
    s=0
    l=eval(input("Enter no :"))
    for i in l:
        s= s + i
    print("Sum of list :",s)
Q11()

def Q12():
    #max from the list
    m=0
    l= eval(input("Enter no :"))
    for i in l:
        if i>m:
            m=i
    print("Max number :",m)
Q12()

def Q13():
    #smallest element
    m=0
    l=eval(input("Enter no :"))
    for i in l:
        if i<m:
            m=i
    print("Min number :",m)
Q13()

def Q14():
    #second largest element
    l=eval(input("Enter no :"))
    a=(sorted(l))
    b=(a[-2])
    print("Second largest no :",b)   
Q14()

def Q15():
    #second smallest
    l=eval(input("Enter no :"))
    a=(sorted(l))
    b=(a[1])
    print("Second smallest :", b)
Q15()

def  Q16():
    #Remove duplicate from a list
    l=eval(input("Enter :"))
    l1=[]
    for i in l:
        if l not in l1:
            l1.append(i)
    print(l1)
Q16()

def Q17():
    #Reverse list
    l=[3,5,88,99,-87,33,23,75]
    print(l[::-1])
Q17()

def Q18():
    #Ascending order
    l=[3,5,88,99,-87,33,23,75]
    print(sorted(l))
Q18()

def Q19():
    #Descending order
    l=[3,5,88,99,-87,33,23,75]
    a=(sorted(l))
    b= (a[::-1])
    print(b)   
Q19()

def Q20():
    #Average
    s=0
    l=[3,5,88,99,-87,33,23,75]
    for i in l:
        s= s + i
        a= s//2
    print(a)    
Q20()

def Q21():
    #Diff between largest and smallest element in the list
    l=[3,5,88,99,-87,33,23,75]
    a= (sorted(l))
    print(a)
    b=(a[0])-(a[-1])
    print(b)
Q21()

def Q22():
    #find index of given element in list
    l=[3,5,88,99,-87,33,23,75]
    b= int(input("Enter element :"))
    a= l.index(b)
    print(a)    
Q22()

def Q23():
    #find number of occurence of a number in list
    l=[3,5,88,99,-87,33,23,75,88,75,3,5,5,3]
    a= int(input("Enter no :"))
    b= l.count(a) 
    print(b)
Q23()

def Q24():
    #Display the elements which are starting from P
    l=['asc', 'psy', 'pet', 'payal', 'priya', 'maitri', 'kishan', 'meet']
    for i in l:
        if (i[0]=='p'):
            print(i)
Q24()

def Q25():
    #Display name which has 4 characters
    l=['meet', 'reet', 'maitri', 'kishan', 'rupa', 'mihir', 'roop']
    for i in l:
        if (len(i)==4):
            print(i)
Q25()

def Q26():
    #Previous list which is accepting list of names and display the index value
    l=eval(input("Enter a list of names :"))
    n=input("Enter a name:")
    print(l.index(n))
Q26()

def Q27():
    #Multiply all the numbers in list by 3
    l=['amit','suman',4,8,'jack',9]
    for i in l:
        if type(i)==int:
            print(i*3)       
Q27()

def Q28():
    #add all the numbers in list
    l=['keyboard',7, 'Ram',9,'Monitor',11,'mouse']
    a=0
    for i in l:
        if type(i)==int:
            a=a+i
            print("sum:",a)
Q28()

def Q29():
    #Program to convert all odd to even by adding 1
    l=[3,4,1,3,21,7,4,2]
    for i in l:
        if i%2!=0:
            a= i+1
            print(a)
Q29()


def Q30():
    #Multiplies only those elements which are multiplies of 7
    l=[3,21,44,33,27,49,54]
    for i in l:
        a=i%7==0
        print(a)
Q30()

def Q31():
    #concete the elements
    a=''
    l=[12,34,43,2,34]
    for i in l:
        a=a+str(i)
    print(a)
Q31()

def Q32():
    #Display name which has i as second last letter
    l=['amit','suman','sumit','montu','anil']
    for i in l:
        if i[-2]=='i':
            print(i)
Q32()


       
    
        


    

    


        
    



    
    
    
    
                 
        
    


    


    


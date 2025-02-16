def Q1():
    age= eval(input("Age :"))
    if age>= 18:
        print("Eligible for voting")
    else:
        print("Not")
Q1()

def Q2():
    Num= eval(input("Enter No :"))
    if Num%7==0:
        print("Divisible")
    else:
        print("No")
Q2()

def Q3():
    No= eval(input("Enter No :"))
    if No%5==0:
        print("Hello")
    else:
        print("Bye")
Q3()

def Q4():
    No=eval(input("Enter No :"))
    print("Last digit of number", No % 10)
Q4()

def Q5():
    No=eval(input("Enter No :"))
    ld=No%3
    if No%3==0:
        print("Divisible")
    else:
        print("Not")        
Q5()

def Q6():
    Marks=eval(input("Marks :"))
    if Marks>90:
        print("Grade A")
    elif Marks>80 and Marks<=90:
        print("Grade B")
    elif Marks>=60 and Marks<=80:
        print("Grade C")
    elif Marks<=60:
        print("Grade D")
Q6()

def Q7():
    Amt=eval(input("Enter Amt :"))
    if Amt>100000:
        tax= 15/100 * Amt
    elif Amt>50000 and Amt<=100000:
        tax =10/100 * Amt
    elif Amt <=50000:
        tax =5/100 * Amt
    print("Tax to be paid", tax)
Q7()

def Q8():
    a=eval(input("Enter a :"))
    b=eval(input("Enter b :"))
    c=eval(input("Enter c :"))
    d=eval(input("Enter d :"))
    if a>b and c>d:
        print("Correct Logic")
    else:
        print("Not")
Q8()

def Q9():
    City= input("City :")
    if City== "Delhi":
        print("Red fort")
    if City== "Agra":
        print("Taj Mahal")
    if City== "Jaipur":
        print("Jal Mahal")
    else:
        print("Invalid")
Q9()

def Q10():
    No=eval(input("3 digit number:"))
    print("Yes" if len(no) == 3 and no.isdigit() else "No")

Q10()

def Q11():
    Age=eval(input("Enter Age :"))
    if Age>=60:
        print("Senior Citizen")
    else:
        print("Not")
Q11()

def Q12():
    a=eval(input("Enter a :"))
    b=eval(input("Enter b :"))
    if a<b:
        print("Lowest", a)
    else:
        print("Lowest", b)
Q12()

def Q13():
    No=eval(input("Enter No :"))
    if No%2==0 and No%3==0:
        print("Yes")
    else:
        print("No")
Q13()

def Q14():
    a=eval(input("Enter a :"))
    b=eval(input("Enter b :"))
    c=eval(input("Enter c :"))
    if a>b and  a>c:
        print("Largest",a)
    if b>a and b>c:
        print("Largest",b)
    if c>a and c>b:
        print("Largest",c)
Q14()

def Q15():
    Temp=eval(input("Enter Temp :"))
    if Temp>= 100:
        print("Boiling")
    else:
        print("Not")
Q15()

def Q16():
   a= eval(input("Enter age1:"))
   b=eval(input("Enter age2 :"))
   c=eval(input("Enter age3 :"))
   d=eval(input("Enter age4 :"))
   if a<b and a<c and a<d:
       print("Yound",a)
   if b<a and b<c and b<d:
        print("Young",b)
   if c<a and c<b and c<d:
        print("Young",c)
   if d<a and d<b and ed<c:
        print("Young", d)          
Q16()

def Q17():
   a= eval(input("Enter age1:"))
   b=eval(input("Enter age2 :"))
   c=eval(input("Enter age3 :"))
   d=eval(input("Enter age4 :"))
   if a>b and a>c and a>d:
       print("Oldest",a)
   if b>a and b>c and b>d:
        print("Oldest",b)
   if c>a and c>b and c>d:
        print("Oldest",c)
   if d>a and d>b and d>c:
        print("Oldest", d)
Q17()


def Q19():
    AL=input("Enter Al ")
    if AL=='a' or AL=='e' or AL=='i' or AL=='o' or AL=='u':
        print('Vowel')
    else:
        print("Not")
Q19()

def Q20():
    NW= eval(input("Enter No of working days :"))
    NA= eval(input("Enter No of absent days :"))
    Present= NW - NA
    Percentage= (Present / NW)* 100
    if Percentage>=0.75:
        print("Will sit in exam")
    else:
        print("Will not sit in exam")
Q20()

def Q21():
    No= eval(input("Enter Marks :"))
    if No>=80:
        print("A +",No)
    elif No>=60 and No<80:
        print("A", No)
    elif No>=50 and No<60:
        print("B+", No)
    elif No>=45 and No<50:
        print("B", No)
    elif No>=25 and No<45:
        print("C", No)
    elif No<25:
        print("D", No)
Q21()

def Q22():
    Salary= eval(input("Enter Salary :"))
    Years= eval(input("Enter Years :"))
    if Years>10:
        Bonus= 0.1 * Salary
    if Years>=6 and Years<=10:
        Bonus= 0.08 * Salary
    if Years <6:
        Bonus= 0.05 * Salary
    print("Net Bonus amt",Bonus)
Q22()

def Q23():
    Market_Price= eval(input("Market Price :"))
    if Market_Price>1000:
        Discount = 0.20 * Market_Price
    elif (Market_Price>7000) and (Market_Price<=10000):
        Discount = 0.15 * Market_Price
    elif Market_Price <=7000:
        Discount = 0.10 * Market_Price
    NA= Market_Price - Discount
    print("Net amount", NA)
Q23()

def Q24():
    Marks= eval(input("Marks: "))
    if  Marks>=65:
        print("Excellent")
    if Marks >=55 and Marks<65:
        print("Good")
    if Marks >=40 and Marks<55:
        print("Fair")
    if Marks<40:
        print("Failed")
Q24()

def Q25():
    a=eval(input("side 1"))
    b=eval(input("side 2"))
    c=eval(input("side 3"))
    if (a==b==c):
        print("Equi")
    if (a==b or b==c or c==a):
        print("Isosceles")
    if (a!=b!=c): 
        print("Scalene")
Q25()

def Q26():
    a= 7
    b= 9
    c= a +b
    print("Addition",c)
    c= a-b
    print("Substraction",c)

    c= a*b
    print("Multiplication",c)

    c= a/b
    print("Division",c)
Q26()

def Q27():
    Days= eval(input("Days :"))
    Age= eval(input("Age :"))
    Gender=input("Gender M/F:")
    if (Age>=18 and Age<30) and (Gender== 'M'):
        Amt= 700 * Days
        print("Wage",Amt)
    elif (Age>=18 and Age<30) and (Gender=='F'):
        Amt= 750 * Days
        print("Wage",Amt)
    elif (Age>=30 and Age<=40) and (Gender=='M'):
        Amt= 800 * Days
        print("Wage", Amt)
    elif (Age>=30 and Age<=40) and (Gender=='F'): 
        Amt= 850 * Days
        print("Wage", Amt)
    else:
        print("Enter appropriate age")
        
Q27()

def Q28():
    a=eval(input(" No 1 :"))
    b=eval(input(" No 2 :"))
    c=eval(input(" No 3 :"))
    if (a>b and a<c) or (a<b and a>c):
        print("Largest", a)
    if (b>c and b<a) or (b<c and b>a):
        print("Largset", b)
    if (c>a and c<b) or (c<a and c>b):
        print("Largest", c)
Q28()

def Q29():
    a= eval(input("side1"))
    b= eval(input("side2"))
    c=eval(input("side2"))
    if (a + b > c) and (b + c > a) and (c + a > b):
        print('valid')
    else:
        print('not')
Q29()

def Q30():
    units=eval(input("units"))
    if (units<=100):
        Bill= 0 
    elif  (units<=300):
        Bill= (units - 100) *  2
    else:
        Bill= (200 * 2)+((units - 300)*5)
    print(" Electricity Bill", Bill)
Q30()

def Q31():
    Days=eval(input("Days"))
    if Days <=5:
        c= Days *2
    if Days>=6 and Days<=10:
        c= Days * 3
    if Days>=11 and Days<= 4:
        c= Days * 4
    if Days>15:
        c= Days* 5
    print(c)
# Q31()

def Q32():
    km=eval(input("km"))
    if km<=10:
        b= km * 11
    if km>=11 and km<=100:
        b= km * 10
    if km>100:
        b= km * 9
    print(b)
Q32()

def Q33():
    E= eval(input("E"))
    M= eval(input("M"))
    S= eval(input("S"))
    SS= eval(input("SS"))
    if (E>80) and (M>80) and (S>80):
        print('Science')
    if (E>80) and (M>80):
        print('Commerce')
    if (E>80) and (SS>80):
        print('Humanities')
    else:
        print("No specific stream suggestion")
Q33()

def Q34():
    a= eval(input("Enter no :"))
    b= eval(input("Enter no :"))
    if a > b:
        print("Is maximum", a)
    else:
        print("Is maximum", b)
Q34()

def Q35():
    a=eval(input("Enter no :"))
    b=eval(input("Enter no :"))
    c=eval(input("Enter no :"))
    if a > b and a > c:
        print("Max",a)
    if b>a and b>c:
        print("Max",b)
    if c>a and c>b:
        print("Max",c)

Q35()

def Q36():
    a=eval(input("Enter no :"))

    if a>0:
        print("Positive")
    if a<0:
        print("Negative")
    else:
        print("Zero")
Q36()

def Q37():
    a=eval(input("Enter no :"))
    if a%5==0 or a%11==0:
        print("Yes")
    else:
        print("No")
Q37()

def Q38():
    a=eval(input("Enter no :"))
    if a%2==0:
        print("Even")
    else:
        print("Odd")
Q38()

def Q39():
    a=eval(input("Enter no :"))
    if a%4==0:
        print("Leap year")
    else:
        print("Not")
Q39()

def Q40():
    c=(input("Enter "))
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        print("Yes", c)
    else:
        print("No", c)
Q40()

def Q41():
    choice=input("Enter :")
    if choice in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonent")
Q41()

def Q42():
    c= input("Enter :")
    if (c>='a' or c>='A') and (c>='z' or c>='Z'):
        print("Alphabet")
    elif (c>='0' or c>='9'):
        print("Digit")
    else:
        print("Character")
Q42()

def Q43():
    c= input("Enter :")
    if (c>='a' and c<='z'):
        print("Lowercase")
    else:
        print("Uppercase")
Q43()

def Q44():
    c= input("Enter :")
    if (c<='1'):
        print("Monday")
    elif(c<='2'):
        print("Tuesday")
    elif(c<='3'):
        print("Wednesday")
    elif(c<='4'):
         print("Thursday")
    elif (c<='5'):
        print("Friday")
    elif(c<='6'):
        print("Saturday")
    elif(c<='8'):
        print("Sunday")
    else:
        print("Please Enter Valid No ")
Q44()

def Q45():
    c=input("Enter")
    if (c=='1'):
        print(31, "days")
    elif(c=='2'):
        print(28, "days")
    elif(c=='3'):
        print(31, "days")
    elif(c=='4'):
        print(30, "days")
    elif(c=='5'):
        print(31, "days")
    elif(c=='6'):
        print(30, "days")
    elif(c=='7'):
        print(31, "days")
    elif(c=='8'):
        print(31, "days")
    elif(c=='9'):
        print(30, "days")
    elif(c=='10'):
        print(31, "days")
    elif(c=='11'):
        print(30, "days")
    elif(c=='12'):
        print(31, "days")
    else:
        print("Enter Valid no")   
Q45()

def Q46():
    amt=eval(input("Enter :"))
    if amt>=500:
        a= amt//500
        amt= amt % 500
        print("500 Rs :", a, "Notes")
    if amt>=200:
        b=amt//200
        amt=amt%200
        print("200 Rs :", b, "Notes")
    if amt>=100:
        c=amt//100
        amt=amt%100
        print("100 Rs :", c, "Notes")
    if amt>=50:
        d=amt//50
        amt=amt%50
        print("50 Rs :", d, "Notes")
    if amt>=20:
        e=amt//20
        amt=amt%20
        print("20 Rs :", e, "Notes")
    if amt>=10:
        f=amt//10
        amt=amt%10
        print("10 Rs :", f, "Notes")
Q46()

def Q47():
    a=eval(input("Enter :"))
    b=eval(input("Enter :"))
    c=eval(input("Enter :"))
    if (a+b+c==180):
        print("Triangle is valid")
    else:
        print("Not")
Q47()

def Q48():
    a= eval(input("Enter :"))
    b= eval(input("Enter :"))
    c=eval(input("Enter :"))
    ans= (a + b)
    if (ans>c):
        print("Valid")
    else:
        print("Not")
Q48()

def Q49():
    a= eval(input("Enter :"))
    b= eval(input("Enter :"))
    c= eval(input("Enter :"))
    if (a==b==c):
        print("Equilateral")
    elif (a==b or a==c or b==c):
        print("Isoceleces")
    else :
        print("Scalene")
    
Q49()

def Q50():
    a=eval(input("Enter SP:"))
    b=eval(input("Enter CP:"))
    
    if a> b:
        print("Profit")
    else:
        print("Loss")
Q50()

def Q51():
    Physics=eval(input("Physics :"))
    if (Physics>= 90):
        print("Grade A")
    elif (Physics>= 80):
        print("Grade B")
    elif (Physics>= 70):
        print("Grade C")
    elif (Physics>= 60):
        print("Grade D")
    elif (Physics>= 40):
        print("Grade E")
    else:
        print("fail")
        
    Chemistry=eval(input("Chemistry :"))
    if (Chemistry>= 90):
        print("Grade A")
    elif (Chemistry>= 80):
        print("Grade B")
    elif (Chemistry>= 70):
        print("Grade C")
    elif (Chemistry>= 60):
        print("Grade D")
    elif (Chemistry>= 40):
        print("Grade E")
    else:
        print("fail")
        
    Bio=eval(input("Bio :"))
    if (Bio>= 90):
        print("Grade A")
    elif (Bio>= 80):
        print("Grade B")
    elif (Bio>= 70):
        print("Grade C")
    elif (Bio>= 60):
        print("Grade D")
    elif (Bio>= 40):
        print("Grade E")
    else:
        print("fail")
        
    Maths=eval(input("Maths :"))
    if (Maths>= 90):
        print("Grade A")
    elif (Maths>= 80):
        print("Grade B")
    elif (Maths>= 70):
        print("Grade C")
    elif (Maths>= 60):
        print("Grade D")
    elif (Maths>= 50):
        print("Grade E")
    else:
        print("fail")
        
    Computer=eval(input("Computer :"))
    if (Computer>= 90):
        print("Grade A")
    elif (Computer>= 80):
        print("Grade B")
    elif (Computer>= 70):
        print("Grade C")
    elif (Computer>= 60):
        print("Grade D")
    elif (Computer>= 40):
        print("Grade E")
    else:
        print("fail")
Q51()

def Q52():
    Salary= int(input("Salary :"))
    if (Salary <=10000):
        HRA= 0.2 + Salary
        DA= 0.8 + Salary
        Gross= Salary + HRA + DA
    elif Salary<=20000:
        HRA=0.25 + Salary
        DA= 0.9 + Salary
        Gross= Salary + HRA + DA
    elif Salary> 20000:
        HRA= 0.3 + Salary
        DA= 0.95 + Salary
        Gross= Salary + HRA + DA
    print(Gross)
Q52()
    
def Q53():
    Units= eval(input("Units :"))
    Surcharge= 0.2
    if (Units<=50):
        Amt= (0.50 * Units)
    elif (Units>=50 and Units<=150):
        Amt= 25 +(Units- 50)* 0.75
    elif (Units>=151 and Units<=250):
        Amt= 100 + (Units- 250) * 1.20
    else :
        Amt= 220 +(Units- 250) * 1.50
    Surchar= Amt * 0.20
    Total= Amt + Surcharge
    print(Total)
Q53()


        




    

              
    

        

              
        
    
    

    
    


    
    
    


    
    
    
    

        
    


    
    
        
    
        
    

    
              



              
        
    

        

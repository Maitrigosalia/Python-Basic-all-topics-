#Application Questions
def Q1():
    #Count number of vowels in a string
    s='maitri'
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count= count + 1       
    print(count)
Q1()

def Q2():
    #Reverse a string
    s=('maitri')
    print(s[::-1])
Q2()

def Q3():
#Write a program to check if 2 string are anagrams of each other
    a='rawan'
    b='wanar'
    x=sorted(a)
    y=sorted(b)
    if x==y:
        print("Anagram")
    else:
        print("Not")
Q3()

def Q4():
    #Remove duplicate from given string
    s='maitri'
    l=''
    for i in s:
        if i not in l:
            l=l+i
    print(l)
    
Q4()

def Q5():
    #check if a given string is palindrome or not
    s=input("Enter string :")
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not")
Q5()

def Q6():
#Find the length of the longest substring without repeating characters
    s=input("Enter string")
    l=""
    for i in s:
        if i not in l:
            l=l+i
    print(l,"length of substring is",len(l))
   
Q6()
                       
def Q7():
    #Capitalize the first letter of each word in stirng
    s="i live in india"
    b=s.title()
    print(b)
Q7()

def Q8():
    #Write a program to find the most frequent word in a given string
    s=input("Enter string :")
    l=s.split()
    l.sort()
    m=0
    k=""
    for i in l:
        if s.count(i)>m:
            m=s.count(i)
            k=i
            
    print(k," is count:",m)
Q8()

def Q9():
    name='John'
    print("Name is {}".format(name))
Q9()

def Q10():
    age='25'
    print("Age is {}".format(age))
Q10()

def Q11():
    sentence='Hello my name is John and I am 25 years old'
    print("sentence is,{}".format(sentence))
Q11()

def Q12():
    person={'first_key':'John','last_name':'Doe'}
    print("{first_key} {last_name}".format_map(person))
Q12()

def Q13():
    fruit='apple'
    print(fruit[0])
Q13()

def Q14():
    word='hello'
    print(len(word))
Q14()

def Q15():
    sentence='I love to code in Python'
    print(sentence.index('Python'))
Q15()

def Q16():
    sentence='I am learning Python'
    a=sentence.replace('Python','Java')
    print(a)
Q16()

def Q17():
    string='python is awesome'
    print(string.capitalize())
Q17()

def Q18():
    string='hello world'
    print(string.upper())
Q18()

def Q19():
    s=input("Enter string 1 :")
    s1=input("Enter string 2 :")
    print(s in s1)
Q19()

def Q20():
    s=input("Enter string")
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count=count + 1
    print(count)
Q20()

def Q21():
    s=input("Enter string")
    print(len(s))
Q21()

def Q22():
    s=input("Enter string :")
    s1=input("Enter string :")
    print("{} {}".format(s,s1))
Q22()

def Q23():
#Find the first non repeating character
    s=input("Enter string :")
    l=""
    for i in s:
        if s.count(i)==1:
            l=l+i
    print(l)
    print(l[0])
Q23()

def Q24():
    s='maitri'
    print(s.count('i'))
Q24()

def Q25():
    s=input("Enter string :")
    print(s.upper())
    print(s.casefold())
Q25()

def Q26():
    s=input("Enter string :")
    l=''
    for i in s:
        if i!=(' '):
            l=l+i
    print(l)            
Q26()

def Q27():
    g=input("Enter string :")
    l=[]
    c=[]
    s=sorted(g)
    for i in s:
        if i not in l:
            l.append(i)
            c.append(s.count(i))
    max=0
    k=0
    f=0
    for j in range(len(c)):
        if c[j]>max:
            k=f
            max=c[j]
            f=j
    print(l[k])    
Q27()

def Q28():
    s=input("Enter string :")
    l=s.split()
    k=""
    for i in l:
         for j in range(len(i)):
             if len(i)==1:
                 k=k+i[j]
             elif(j==1):
                 k=k+i[j].upper()
             else:
                 k=k+i[j]
         k=k+" "
    print(k)
Q28()

  
    
            
        
    
    

    
    
    
        
        
        
    

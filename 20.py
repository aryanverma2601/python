li = []
li2=[]

num1= int(input("enter 1st number: "))
num2= int(input("enter 2nd number: "))
for i in range(2, num1+1):
    while (num1 != 1):
        if (num1 % i == 0):
            while (num1 % i == 0):
                num1 //= i
                li.append(i)
for i in range(2,num2+1):
    while (num2 != 1):
        if (num2 % i == 0):
            while (num2 % i == 0):
                num2 //= i
                li2.append(i)

  
print(li,li2)

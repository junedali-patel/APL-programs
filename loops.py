def sum():
    num1=1.5
    num2=206
    sum=float(num1)+float(num2)
    print("The Sum is=",sum)
sum()

print ("_____________________________________________________")


num = int (input ("Enter the number"))
if  num%2==0:
    print("Number is even")

print ("_____________________________________________________")


age= int (input("Enter the age "))
if age>=18:
    print("You are eligible for voting")
else:
    print("You ae not eligible for voting")

print("END OF PROGRAM")


print ("_____________________________________________________")


a=int(input("Enter the number"))
if a==10:
    print("Number equal to 10")
elif a==50:
    print("Num equals to 50")
elif a==100:
    print("Num equals to 100")
else:
    print("Num not equals to 10,50 & 100")
print("END OF PROGRAM")

print ("_____________________________________________________")


i=1
while i<=5:
    print(i,end='*')
    i+=1
else:
    print("END OF PROGRAM")

print ("_____________________________________________________")


tuple=(3,4,6,8,9,2,3,8,9,7)
for value in tuple:
    if value %2 != 0:
     print("These are even nos.", value)
else :
    print("These are the odd nos." ,value)

print ("_____________________________________________________")
for n in range(3,6):
    print(n)

print ("_____________________________________________________")
def forloop():
    n= int (input("enter the number"))
    for i in range(0,n):
        print(i)
forloop()
print ("_____________________________________________________")
def length():
    name=input("Enter Name")
    for i in range(0,len(name)):
        print(i)
length()
print ("_____________________________________________________")
for string in "Python loops":
    if string=='l':
        break
    print("Current Letter :",string)
print ("_____________________________________________________")

for string in "Python Loops":
    if string=='o'or string=='P' or string=='t':
        continue
    print("current letter", string)
print ("_____________________________________________________")
def pass_eg():
    for i in range(0,5):
      pass
    print("GOODBYE!!")
pass_eg()
print ("_____________________________________________________")




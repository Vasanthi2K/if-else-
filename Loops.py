''' 
Program to print numbers from 1-10 
i=1
while i<=10:
    print(i)
    i+=1
'''

'''
Program to calculate first 10 Natural numbers

i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)
'''
#Program to print multiplication table of num #
'''
a=int(input())
for i in range(1,11):
    print(i*a)
'''
'''
Factorial Value
num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
'''
'''
Power of another
a=int(input())
b=int(input())
result=1
for b in range(b,0,-1):
    result *= a
print(result)
'''
'''
a=int(input())
b=int(input())
result = pow(a,b)
print(result)
'''
'''
Printing a num in reverse order
num = int(input())
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
'''

'''
num=int(input())
print(str(num)[::-1])
'''

'''
Fibonacci Series
num= int(input())
a=0
b=1
if num == 1:
    print(a)
else :
    print(a)
    print(b)
    for i in range(2, num):
        c=a+b
        a=b
        b=c
        print(c)
'''
'''
Program to check whether a num is prime or not

num=int(input())
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num, "is not a prime num")
            break
    else:
        print(num, "is a prime")
else:
    print(num, "is not a prime")

'''
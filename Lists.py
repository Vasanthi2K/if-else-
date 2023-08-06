'''
List is one of the complex data types.
Its not like that lists should have same type of data. But the data inside the list can be of any type.
But this is not a very common practice. Usually we keep same type of data in a list.
'''
'''
Accessing elements of list one by one

students_list=["Kirithiv", "Vasanthi", "Navgurukul"]
list_length=len(students_list)
index=0
while index<list_length:
    print(students_list[index])
    index = index+1

'''

'''
Calculating total marks

student_marks=[23,45,49,36,42,39]
length=len(student_marks)
index=0
total_marks=0
while index<len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
print(total_marks)

'''
'''
lis=[[]]*4
print(lis)
'''

'''
pop() function of lists deletes the element present at index 
list1=[3,2,5,7,3,6]
list1.pop(3)
print(list1)
'''
'''
  1. we use append() function to add an element to the list.
  2. len funciton count the number of elements in the list.
'''
'''
names=['Kirithiv', 'Vasanthi', 'Koka', 'Aurobindo']
print(names[-1][-1])
'''
'''
Counting elemets in a list without using len() function
name=[50,30,10,25,63,45,43]
count=0
for i in name:
    count+=1
print(count)
'''
'''
Counting the occurance of an element in a list
list1=[3,4,5,20,5,25,1,3]
print(list1.count(5))
'''
'''
Reverse order of items
place=["Chennai", "Andhra", "Kerala", "Bangalore"]
print(place.reverse())
'''
'''
Maximum in the list
num=[96,97,99,120,163]
print(max(num))
'''
'''
l=[1,5,9]
print(sum(l), max(l), min(l))
'''
'''
aList=["PYnative", [4,8,12,16]]
print(aList[0][1])
print(aList[1][3])
'''
'''
marks = [
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]
for i in range(3):
    totalMarks=0
    for j in range(5):
        totalMarks=totalMarks+marks[i][j]
avgMarks=totalMarks/5
print(str(i+1),int(avgMarks))
'''
'''
Sum of even and odd numbers
elements=[23,14,56,12,19,9,15,25,31,42,43]
odd_sum=0
even_sum=0
for sub in elements:
    for item in str(sub):
        if int(item)%2==0:
            even_sum+=int(item)
        else:
            odd_sum+=int(item)
print(odd_sum)
print(even_sum)
'''
'''
l=[23,14,56,12,19,9,15,25,31,42,43]
sumodd=0
sumeven=0
odd=[]
even=[]
allsum=0
l2=len(l)
for i in l:
    allsum+=i
    if(i%2==0):
        sumeven+=i
        even.append(i)
        length=len(even)
    else:
        sumodd+=i
        odd.append(i)
        l2=len(odd)
print("count odd=", l2)
print("count sum=", length)
print("sum of odd=", sumodd)
print("sum of even=", sumeven)
'''
#Extend() function to add the elements to the list.
#Elememts of lists are stored in continuous memory location.

'''
Calculating average
list1=[80,66,94,87,99,95]
print(sum(list1)/len(list1))
'''
'''
list1=["Python", "Java", "c", "C++", "C"]
print(min(list1))
'''
'''
list1=["tom", "mary", "simon"]
list1.insert(5,8)
print(list1)
'''


'''
Counting the occurance of an element without using count()

list1=[3,4,5,20,5,25,1,5,3]
count=0
for i in list1:
    if i == 5:
        count+=1
print(count)

'''

'''
Finding the maximun number without inbuilt function
list=[10,12,15,4,96,105]
max = 0
for i in list:
    if i > max:
        max = i
print (max)
'''

'''
Findind the smallest number without using min()
list=[10,12,15,4,96,105,-9,-999]
min = 1000
for i in list:
    if i < min:
        min = i
print (min)
'''
'''
Printing a num in reverse order
num = (input())
for i in reversed(num):
        print(i, end='')
'''
'''
printing numbers in reverse order without using reverse()
num=int(input())
rev=0
while num>0:
    remainder = num%10
    rev = (rev*10)+remainder
    num = num//10
print(rev)
'''
'''
print(1%10)
'''

'''
1. To find maximum number among elements in list [Don't use inbuilt method]
list=[10,12,15,4,96,105]
max = 0
for i in list:
    if i > max:
        max = i
print (max)
'''
'''
#2. To find minimum number among elements in list [Don't use inbuilt method]
list=[10,12,15,4,96,105]
min = 10000
for i in list:
    if i < min:
        min = i
print (min)
'''
'''
#3. You have been given a list of words and you have to sort them in alphabetical order
The sorted() function is a built-in function in python that takes any iterable like a list and 
returns a new sort list, which is alphabetically sorted.

str=("d,", "a", "f", "c", "b", "e")
x=sorted(str, reverse = False)
print(x)
'''
'''
#Method2
str = ["d","a","b","e"]
str.sort()
print(str)
'''
'''
Program to remove duplicate elements and return list of unique elements from a list
a = [1,2,3,4,4,2,1,6,7]
res = [*set(a)]
print(res)

a = [1,3,3,8,9,1,2,6,2]
res = list(set(a))
print(res)
'''

'''
program to remove all the negative numbers from a list
a = [1,-2,3,-4,-6,7]
res = []
for i in a:
    if i > 0:
        res.append(i)
print(res)
'''
'''
#Program to return odd numbers only.
a = [1,2,3,4,6,7,10]
res = []
for i in a:
    if i % 2 != 0:
        res.append(i)
print(res)
'''



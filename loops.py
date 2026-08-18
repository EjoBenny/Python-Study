'''
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

for i in student:
    print(i)

'''
'''
numbers=[34,11,6,13,8,17]
for num in numbers:
    if num%2==0:
        print(num,"is Even")

'''
'''
lang="Python"

for k in lang:
    print(k)

for j in [45,12,"Ebin"]:
    print(j)

for k in {"name":"Joyal","age":23,45:9}:
    print(k)
'''

'''
numbers=[34,11,6,13,8,17]
even_num=[]
for num in numbers:
    if num%2==0:
        even_num.append(num)
print("Even numbers are:",even_num)
'''


'''
print(list(range(5)))

print(tuple(range(3,10)))

for n in range(3,15,4):
    print(n)
'''

'''
n=int(input("Enter the number : "))
for num in range(1,11):
    print(f"{num} x {n} = {num*n}")

'''
'''
num=int(input("Enter the number : ")) # 5
fact=1
for k in range(1,num+1): # 1 , 2 , 3 , 4 , 5
    fact=fact*k

print("Answer = ",fact)

print("Hi",end=" ")
print("Ebin")
print("Completed")

for n in range(1,11):
    print(n,end=" ")

'''

'''
first=0
second=1
print(first,second,end=" ")
for k in range(8):
    third=first+second
    print(third,end=" ")
    first,second=second,third
'''



'''
f=0
s=1
print(f,s,end=" ")
count=1

while count<=8:
    
    t=f+s
    print(t,end=" ")
    f,s=s,t
    count+=1
'''

'''
num=[1,25,46,79,21,24,44,89,41]
count=0
for i in num:
    if count>=2:
        break
    if i%2==0:
        print(i)
        count+=1
'''
for i in range(1,6):
    print(" "*(i-1),"*"*(6-i))
n=int(input("enter the number of elements in the list:"))
l=[]
for i in range(0,n):
    if i==0:
        l=[int(input())]
    else:
        l.append(int(input()))
print("the list is:")        
print(l)  
print("the positive numbers are:")
for a in l:
    if a>=0:
        print(a,end=",")
        
        
 output:
 enter the number of elements in the list:5
12
-7
5
64
-14
the list is:
[12, -7, 5, 64, -14]
the positive numbers are:
12,5,64,

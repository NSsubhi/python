n=int(input("enter the number of fibonacci elements : "))
l=[0,1]
print("the fibonacci series :",end="")
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
print(l)    


output:
enter the number of fibonacci elements : 15
the fibonacci series :[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

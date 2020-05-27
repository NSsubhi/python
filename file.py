f = input("Input the Filename: ")
l=len(f)
count=0
print("the extension is : ",end='')
for i in f:
    if (i!="."):
        count=count+1
    else:
        for j in range(count+1,l):
            print(f[j],end="")
        
        
        
output:
Input the Filename: abc.txt
the extension is : txt

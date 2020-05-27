import operator
def most_frequent(s):
    d = {}
    k=d.keys()
    for i in s:
        if i in k:
            d[i] += 1
        else:
            d[i] = 1
    sorted_d = dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    print('frequency in descending order : ',sorted_d) 
s=input("enter the string : ")
most_frequent(s)


output:
enter the string : mississippi
 frequency in descending order :  {'i': 4, 's': 4, 'p': 2, 'm': 1}

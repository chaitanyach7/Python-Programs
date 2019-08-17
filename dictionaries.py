a=['a','b','c']
a={i:0 for i in a}
x=[1,2,3,4]
x=dict((i,2) for i in x )
print(a,x)
x[2]+=1
print(x)

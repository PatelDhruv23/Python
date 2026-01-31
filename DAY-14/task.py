#----------------------------------------------
#! d = [{'tesla':{'model':'x','color':'red'}},
#!      {'audi':{'model':'y','color':'black'}}]

d = [{'tesla':{'model':'x','color':'red'}},
    {'audi':{'model':'y','color':'black'}}]

input1 = list(d[0].keys())
input2 = list(d[1].keys())

print(input1) 
print(input2)

out=[]

for i,j in zip(input1,input2):
    out.append(d[0][i])
    out.append(d[1][j])

print(out)


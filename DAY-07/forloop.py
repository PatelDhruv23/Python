
#In String
print('For Loop in String')
for i in 'Dhruv':
    print(i)

#In List
print('For Loop in List')
for i in [1,2,3,'Python']:
    print(i)

#In Tuple
print('For Loop in Tuple')
for i in (1,2,3,'python'): 
    print(i)

#In Set
print('For Loop in Set')
for i in {10,1,'Python',3+3j}:
    print(i)

#In Dict
print('For Loop in Dict')
for i in {'A':10,'B':20,'C':30}:
    print(i)

a={'A':10,'B':20,'C':30}
for i in a:
    print(a[i])

for i in a.items():
    print(i)

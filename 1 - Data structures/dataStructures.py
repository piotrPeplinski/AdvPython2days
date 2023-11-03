#LIST
List = [1,2,3,5,2]

powers = []
for number in List:
    if number%2==0:
        powers.append(number**2)

powers_exp = [number**2 for number in List if number % 2 == 0]
#print(powers_exp)
#0,1,...
#-1

# List.append('Piotr')

# List.insert(2, 'First')
# List.remove(2)


#TUPLE 
Tuple = (1,2,3,4)
numbers = tuple(List)

dataset = list(Tuple)
dataset.append(3)

generator = (
    number
    for number in range(5)
)

print(next(generator))
print(next(generator))

#DICT
Dict = {'Name': 'Python', 'Lib':'Pandas'}
Dict['Trainer'] = 'Peter'

names = ['Peter','Alice','Robert']
# names_length = {
#     name:len(name)
#     for name in names
# }
#del Dict['Lib']
#print(Dict.pop('Lib'))
#print(Dict)

#SET
# Set = {1,2,3,4,4}
# #print(list(set(List)))
# Set = {
#     number+1
#     for number in range(10)
#     if number % 2 == 0
# }
# print(Set)
# Set.add(67)

# empty = set()
# print(type(empty))
# print(empty)
a = {1,2,3,4}
b = {3,4,5,6}

a_immut = frozenset(a)
print(set(a_immut&b))

# #UNION +
# print(a | b)
# #print(a.union(b))

# #INTERSECTION
# print(a & b)

# #DIFFERENCE -
# print(a-b)

# #SYMETRIC DIFFERENCE
# print(a^b)







tuplex  =(False,"Hello",12,45.23)
print(tuplex)

tuplex = (4,3,9,3,9,0,4,9,2,6,7,2,4,3,3,2,5,2)
print(tuplex)
tuplex = tuplex + (8,)
print(tuplex)

tuples = tuplex.count(2)
print(tuples)

slice = tuplex[4:10]
print(slice)
slice1 = tuplex[:8]
print(slice1)
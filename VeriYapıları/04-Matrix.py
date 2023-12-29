# matrix : list of list

# tek boyutlu liste
l = [1,2,3] 

# iki boyutlu
m = [ [1,2,3,4], [4,5,6], l ] # l, buraya shallow copy olur 

print(m)
l[0] = 100
print(m)
print()


matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
mt = [[row[i] for row in matrix] for i in range(3)] #matrix'in transpozunu alır (sutunlar satır, satırlar sutun olur)
print(matrix)
print(mt)

# silme islemleri
del(matrix[1]) 
mt.pop(1)
print(matrix)
print(mt)
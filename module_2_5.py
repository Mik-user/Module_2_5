def get_matrix(n,m,value):
    matrix = list()
    for i in range(n):
        x = list()
        for j in range(m):
            x.append(value)
        matrix.append(x)
    return matrix
rezult1 = get_matrix(2,3,9)
rezult2 = get_matrix(4,6,8)
rezult3 = get_matrix(3,3,7)
print(rezult1)
print(rezult2)
print(rezult3)

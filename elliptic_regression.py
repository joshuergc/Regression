import math
import numpy as np

def f(x):
    temporal = str(x).split(".")
    if len(temporal[1]) >= 6:
        temporal[1] = temporal[1][0:6]
    temporal1 = ".".join(temporal)
    return float(temporal1)

temporal_1 = list(map(float, input().split(",")))

x, y = temporal_1[0], temporal_1[1]

n = int(input())

n_pares = []

for i in range(n):
    temporal_2 = list(map(float, input().split(",")))
    n_pares.append(temporal_2)
    
print()

n_puntos = []

for i in range(n):
    temporal_3 = []
    temporal_3.append(x+n_pares[i][1]*math.cos(math.atan(n_pares[i][0])))
    temporal_3.append(y+n_pares[i][1]*math.sin(math.atan(n_pares[i][0])))
    n_puntos.append(temporal_3)
    temporal_3 = []
    temporal_3.append(x-n_pares[i][1]*math.cos(math.atan(n_pares[i][0])))
    temporal_3.append(y-n_pares[i][1]*math.sin(math.atan(n_pares[i][0])))
    n_puntos.append(temporal_3)
    
for i in range(len(n_puntos)):
    n_puntos[i][0] = f(n_puntos[i][0])
    n_puntos[i][1] = f(n_puntos[i][1])

for i in n_puntos:
    print(i[0], i[1], sep=",")
    
n = len(n_puntos)

matrix_list = []
vector_list = []

j = [0, 0, 0, 0, 0, 0]
for i in range(n):
    j[0] = j[0]+n_puntos[i][0]*n_puntos[i][1]*(n_puntos[i][0]*n_puntos[i][1])
    j[1] = j[1]+n_puntos[i][1]*n_puntos[i][1]*(n_puntos[i][0]*n_puntos[i][1])
    j[2] = j[2]+n_puntos[i][0]*(n_puntos[i][0]*n_puntos[i][1])
    j[3] = j[3]+n_puntos[i][1]*(n_puntos[i][0]*n_puntos[i][1])
    j[4] = j[4]+1*(n_puntos[i][0]*n_puntos[i][1])
    j[5] = j[5]+n_puntos[i][0]*n_puntos[i][0]*(n_puntos[i][0]*n_puntos[i][1])

temporal_4 = []
for i in range(5):
    temporal_4.append(j[i])
    
matrix_list.append(temporal_4)
vector_list.append(-j[5])

j = [0, 0, 0, 0, 0, 0]
for i in range(n):
    j[0] = j[0]+n_puntos[i][0]*n_puntos[i][1]*(n_puntos[i][1]*n_puntos[i][1])
    j[1] = j[1]+n_puntos[i][1]*n_puntos[i][1]*(n_puntos[i][1]*n_puntos[i][1])
    j[2] = j[2]+n_puntos[i][0]*(n_puntos[i][1]*n_puntos[i][1])
    j[3] = j[3]+n_puntos[i][1]*(n_puntos[i][1]*n_puntos[i][1])
    j[4] = j[4]+1*(n_puntos[i][1]*n_puntos[i][1])
    j[5] = j[5]+n_puntos[i][0]*n_puntos[i][0]*(n_puntos[i][1]*n_puntos[i][1])

temporal_4 = []
for i in range(5):
    temporal_4.append(j[i])
    
matrix_list.append(temporal_4)
vector_list.append(-j[5])

j = [0, 0, 0, 0, 0, 0]
for i in range(n):
    j[0] = j[0]+n_puntos[i][0]*n_puntos[i][1]*(n_puntos[i][0])
    j[1] = j[1]+n_puntos[i][1]*n_puntos[i][1]*(n_puntos[i][0])
    j[2] = j[2]+n_puntos[i][0]*(n_puntos[i][0])
    j[3] = j[3]+n_puntos[i][1]*(n_puntos[i][0])
    j[4] = j[4]+1*(n_puntos[i][0])
    j[5] = j[5]+n_puntos[i][0]*n_puntos[i][0]*(n_puntos[i][0])

temporal_4 = []
for i in range(5):
    temporal_4.append(j[i])
    
matrix_list.append(temporal_4)
vector_list.append(-j[5])

j = [0, 0, 0, 0, 0, 0]
for i in range(n):
    j[0] = j[0]+n_puntos[i][0]*n_puntos[i][1]*(n_puntos[i][1])
    j[1] = j[1]+n_puntos[i][1]*n_puntos[i][1]*(n_puntos[i][1])
    j[2] = j[2]+n_puntos[i][0]*(n_puntos[i][1])
    j[3] = j[3]+n_puntos[i][1]*(n_puntos[i][1])
    j[4] = j[4]+1*(n_puntos[i][1])
    j[5] = j[5]+n_puntos[i][0]*n_puntos[i][0]*(n_puntos[i][1])

temporal_4 = []
for i in range(5):
    temporal_4.append(j[i])
    
matrix_list.append(temporal_4)
vector_list.append(-j[5])

j = [0, 0, 0, 0, 0, 0]
for i in range(n):
    j[0] = j[0]+n_puntos[i][0]*n_puntos[i][1]
    j[1] = j[1]+n_puntos[i][1]*n_puntos[i][1]
    j[2] = j[2]+n_puntos[i][0]
    j[3] = j[3]+n_puntos[i][1]
    j[4] = j[4]+1.0
    j[5] = j[5]+n_puntos[i][0]*n_puntos[i][0]

temporal_4 = []
for i in range(5):
    temporal_4.append(j[i])
    
matrix_list.append(temporal_4)
vector_list.append(-j[5])

matrix_square = np.array(matrix_list)
vector = np.array(vector_list)

solution = np.linalg.solve(matrix_square, vector)

print()
print(list(solution))

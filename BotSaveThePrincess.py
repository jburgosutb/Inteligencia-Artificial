#!/usr/bin/env python
# coding: utf-8

# In[41]:


from collections import deque 
import random


# In[42]:


def busqueda(n, tablero , fila_r, col_r, fila_p, col_p):
    visitado = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((fila_r, col_r, []))

    while queue:
        fila, col, mov = queue.popleft()
        visitado[fila][col] = True
        current_tablero = [fila[:] for fila in tablero]

        if fila == fila_p and col == col_p:
            return mov, current_tablero

        
        coordenadas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direcciones = ["UP", "DOWN", "LEFT", "RIGHT"]

        for (df, dc), move in zip(coordenadas, direcciones):
            nueva_fila, nueva_col = fila + df, col + dc
            if 0 <= nueva_fila < n and 0 <= nueva_col < n and not visitado[nueva_fila][nueva_col]:
                nuevo_mov = mov + [move]
                queue.append((nueva_fila, nueva_col, nuevo_mov))


# In[43]:


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


# In[46]:


def siguiente(n, fila_r, col_r, tablero, fila_p, col_p):
    pos_r = [fila_r, col_r]
    pos_p = [fila_p, col_p]
    
    
    mov, final_tablero = busqueda(n, tablero, pos_r[0], pos_r[1], pos_p[0], pos_p[1])
    
    
    for move in mov:
        if move == "UP":
            fila_r -= 1
            print("UP")
        elif move == "DOWN":
            fila_r += 1
            print("DOWN")
        elif move == "LEFT":
            col_r -= 1
            print("LEFT")
        elif move == "RIGHT":
            print("RIGT")
            col_r += 1
            
        for i in range(n):
            for j in range(n):
                if i == fila_r and j == col_r:
                    tablero[i][j] = "b"
                    
                elif i == fila_p and j == col_p:
                    tablero[i][j] = "p"
            
                else:
                    tablero[i][j] = "."


        print_grid(tablero)

    return mov, final_tablero


# In[50]:


n = int(input ("Defina el tamaño de su matriz cuadrada:"))

row_bot = random.randint(0, n -1) 
col_bot = random.randint(0, n - 1) 
row_p = random.randint(0, n -1)
col_p = random.randint(0, n - 1)

tablero = [["." for i in range(n)] for j in range(n)]

tablero[row_bot][col_bot] = "b"
tablero[row_p][col_p] = "p"

for i in range(n):
    for j in range(n):
        print(tablero[i][j], end=" ")
    print()  
print()

mov, final_tablero = siguiente(n, row_bot, col_bot, tablero, row_p, col_p)


# In[ ]:





coordernadas = [(1,1),(3,2),(2,4),(0,4)]
pos_atual = (3,0)
lista = []
caminhos = []
coordernadas2 = []
caminho_total = 0
for i in coordernadas:
    x = pos_atual[0] - i[0]
    y = pos_atual[1] - i[1]
    soma = abs(x) + abs(y) 
    lista.append([i,soma]) 
for t in lista:
    if min(caminhos.append(t[1])):
        print(lista[0]) 

# import itertools
# valor_caminhos = [] 

# def permutacao(num1,num2,num3,num4):
#     permutations = list(itertools.permutations([num1,num2,num3,num4], 4)) 
#     return permutations

# def calcular_caminhos():
#     coordenadas = permutacao((1,1),(3,2),(2,4),(0,4))
#     for pontos in coordenadas:
#         pontos = list(pontos) 
#         posicao_atual = (3,0) 
#         distancia_total = 0 
#         quantidade_pontos = len(pontos)
#         for i in range(0,quantidade_pontos+1):
#             lista_coordenada_caminho = []
#             if pontos == []:
#                 pontos.append((3,0))
#             for ponto in pontos:
#                 x = posicao_atual[0] - ponto[0]
#                 y = posicao_atual[1] - ponto[1]
#                 soma = abs(x) + abs(y) 
#                 lista_coordenada_caminho.append((ponto,soma)) 
#             print(lista_coordenada_caminho) 
#             caminho_minimo = lista_coordenada_caminho[0][1] 
#             posicao_atual = lista_coordenada_caminho[0][0]
#             distancia_total += caminho_minimo
#             pontos.remove(posicao_atual)      
#         valor_caminhos.append(distancia_total)        
#     return valor_caminhos


# calcular_caminhos()
# #print(f'Caminhos:{valor_caminhos}') 
# print(f'Caminho mínimo:{min(valor_caminhos)}')
 
# value = min(valor_caminhos) 
# for z, v in enumerate(valor_caminhos): 
#     if v == value: 
#         coordenadas = permutacao('A','B','C','D') 
#         print(f'Rota:{list(coordenadas[z])}')  













# for z, v in enumerate(valor_caminhos): 
#     coordenadas = permutacao('A','B','C','D') 
#     print(f'Rota {z+1}: {list(coordenadas[z])}  Distância: {v}')  
# for i in range(1,4):
#     print(i)
 
# caminho_total = 0
# pontos = [(1,1),(3,2),(2,4),(0,4)]
# quantidade_pontos = len(pontos)
# pos_atual = (3,0) 

# for i in range(0,quantidade_pontos+1):
#     lista = []
#     if pontos == []:
#         pontos.append((3,0))
#     for ponto in pontos:
#         x = pos_atual[0] - ponto[0]
#         y = pos_atual[1] - ponto[1]
#         soma = abs(x) + abs(y) 
#         lista.append((ponto,soma)) 
#     sorted_lst = sorted(lista, key=lambda x: x[1])
#     caminho_minimo = sorted_lst[0][1] 
#     pos_atual = sorted_lst[0][0]
#     caminho_total += caminho_minimo
#     pontos.remove(pos_atual)
#     print(f'Lista ordenada:{sorted_lst}')
#     print(f'Posição atual:{pos_atual}') 
#     print(f'Caminho mínimo:{caminho_minimo}')
#     print(f'Caminho Total:{caminho_total}\n')
    


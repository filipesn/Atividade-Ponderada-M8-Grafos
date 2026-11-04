# Atividade-Ponderada-M8-Grafos

Atividade de Grafos.

Primeira coisa feita foi pegar meu RA

A2025.1A.0188

Então de valores serão 5, 1, 0, 1, 8 e 8

Começei com Dijkstras. Com uma pesquisa na internet, achei um exemplo:

https://medium.com/@storiesofsrinidhi/visualizing-dijkstras-algorithm-with-networkx-and-matplotlib-a7a375fd0731

Parece está funcionando. Darei uma olhada depois. Agora, devo montar a tabela.`

Aqui a normal

D1 5 D2 1 D3 0 D4 1 D5 8 D6 8

Aresta Ramal Fórmula do peso w(e) Exemplo (RA 210854)
e1 (S0, S1) w1 = 10 + (D6 mod 5) 10 + (4 mod 5) = 14 km
e2 (S0, S2) w2 = 15 + (D5 mod 7) 15 + (5 mod 7) = 20 km
e3 (S1, S2) w3 = 8 + (D4 mod 4) 8 + (8 mod 4) = 8 km
e4 (S1, S3) w4 = 12 + (D3 mod 6) 12 + (0 mod 6) = 12 km
e5 (S2, S4) w5 = 14 + (D2 mod 5) 14 + (1 mod 5) = 15 km
e6 (S2, S5) w6 = 9 + (D1 mod 6) 9 + (2 mod 6) = 11 km
e7 (S3, S4) w7 = 7 + ((D5 + D6) mod 5) 7 + (9 mod 5) = 11 km
e8 (S3, S6) w8 = 11 + ((D4 + D5) mod 6) 11 + (13 mod 6) = 12 km
e9 (S4, S5) w9 = 6 + ((D3 + D4) mod 4) 6 + (8 mod 4) = 6 km
e10 (S4, S7) w10 = 16 + ((D2 + D3) mod 7) 16 + (1 mod 7) = 17 km
e11 (S5, S7) w11 = 18 + ((D1 + D2) mod 8) 18 + (3 mod 8) = 21 km
e12 (S6, S7) w12 = 9 + ((D5 + D1) mod 5) 9 + (7 mod 5) = 11 km
e13 (S1, S4) w13 = 20 + (D6 mod 4) 20 + (4 mod 4) = 20 km

Para calcular, mandei tudo na linha de commando do python. O primeiro rodou assim, e fiz isso para todos os outros:

PS C:\Users\Fi\Documents\Atividade-Ponderada-M8-Grafo> 10+(8%5)
13
PS C:\Users\Fi\Documents\Atividade-Ponderada-M8-Grafo>

e1 (S0, S1) w1 = 13
e2 (S0, S2) w2 = 16
e3 (S1, S2) w3 = 9
e4 (S1, S3) w4 = 12
e5 (S2, S4) w5 = 15
e6 (S2, S5) w6 = 14
e7 (S3, S4) w7 = 8
e8 (S3, S6) w8 = 14
e9 (S4, S5) w9 = 7
e10 (S4, S7) w10 = 17
e11 (S5, S7) w11 = 24
e12 (S6, S7) w12 = 12
e13 (S1, S4) w13 = 20

Me senti um escravo fazendo isso

Agora vamos fazer o grafo

Eu fiz o desenho. Está como "grafo.png" no repositorio

Apos isso eu fiz a matriz. Está salvo como matriz.jpeg

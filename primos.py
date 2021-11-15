#Um número é, por definição, primo se ele não tem divisores,
#exceto 1 e ele próprio. Escreva um programa que leia
# um número e determine se ele é ou não primo.

n = int(input().strip())
t = 0
for c in range(1, n + 1):
    if n % c == 0 :
        t+=1

if t == 2:
    print('True')
else:
    print('False')
    
    

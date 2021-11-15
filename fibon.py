fibo = int(input().strip())
numero1= 0
numero2= 1
cont = soma = 0
for i in range( 0, fibo):
    numero1 = numero2
    numero2 = soma
    print(f'{numero2}', end=", " if cont< fibo -1 else ' ')
    soma = numero1 + numero2
    cont = cont + 1  
   

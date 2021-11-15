divisao = 0
a = 1
b = 1
soma = 0
n = int(input().strip())
while soma < n:
    b+=1
    divisao = a / b
    soma +=divisao
    if b >=n:break
print(f'{1+soma:.4f}')

def eh_primo(n):
    i=1
    cont=0
    while i<=n:
        if n%i==0:
            cont+=1
        i+=1
    if cont>2:
        return False
    else:
        return True


def main():
    x=int(input())
    y=int(input())

    while x<=y:
        if eh_primo(x)==True:
            print(x)
        x+=1

if __name__=='__main__':
    main()

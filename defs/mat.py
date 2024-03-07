
def soma():
    a = float(input("Digite o primeiro número para somar:  "))
    b = float(input("Digite o segundo número para somar :  "))
    c = a + b
    return (c)

def potencia():
    a = float(input("Digite a base     :  "))
    b = float(input("Digite o expoente :  "))
    c = a**b
    return (c)

def fibonacci():
    a = int(input("Digite até qual termo deseja ir:  "))
    if (a > 0):
        return (calcFib(a))
    
def calcFib(x):
    fib = [1,1]
    if (x == 1 or x == 2):
        return (1)
    else:
        for i in range(2,x+1):
            valorFib = fib[i-2]+fib[i-1]
            fib.append(valorFib)
        return (valorFib)


def fib2(a):
    if ((a == 1) or (a == 2)):
        fib = 1
    else:
        fib = fib2(a-2) + fib2(a-1)
    return (fib)

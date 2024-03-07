'''1
print("Hola mundo")
'''

'''2
print(3+5)
'''

'''3
nombre = input("Ingrese su nombre: ")
print("Hola", nombre)
'''
'''4
num_1 = input("Ingrese el primer numero: ")
num_2 = input("Ingrese el segundo numero: ")
num_1 = float(num_1)
num_2 = float(num_2)

resultado = num_1 + num_2

print("El resultado es: ", resultado)
'''
''''''
'''5

num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num1 = float(num1)
num2 = float(num2)

if num1>num2 : 
    print(num1," es mayor que ", num2)
else: print(num2," es mayor que ", num1)
'''

'''6

numm1 = input("Ingrese el primer numero: ")
numm2 = input("Ingrese el segundo numero: ")
numm3 = input("Ingrese el tercer numero: ")
numm1 = float(numm1)
numm2 = float(numm2)
numm3 = float(numm3)

if numm1>numm2 and numm1>numm3:
    print(numm1," es el mayor de los tres numeros ingresados")
elif numm2>numm1 and numm2>numm3:
    print(numm2," es el mayor de los tres numeros ingresados")
else :
    print(numm3," es el mayor de los tres numeros ingresados")
'''

'''7

numero = input("Ingrese un numero: ")
numero = int(numero)

if ((numero%2) == 0) :
    print("El numero ingresado SI es divisible por 2")
else :
    print("El numero ingresado NO es divisible por 2")
    
'''

'''8

numero = input("Ingrese un numero: ")
numero = int(numero)

if ((numero%2) ==0):
    print("Es divisible por 2")
elif ((numero%3) ==0):
    print("Es divisible por 3")
elif ((numero%5) ==0):
    print("Es divisible por 5")
elif ((numero%7) ==0):
    print("Es divisible por 7")
else: print("NO es divisible")
'''

'''9

numero = input("Ingrese un numero: ")
numero = int(numero)

if ((numero%2) ==0 or (numero%3) ==0 or (numero%5) ==0 or (numero%7) ==0):
    if (numero%2) ==0:
        print("Es divisible por 2")
    if ((numero%3) ==0):
        print("Es divisible por 3")
    if ((numero%5) ==0):
        print("Es divisible por 5")
    if ((numero%7) ==0):
        print("Es divisible por 7")
else: print("NO es divisible por ningun numero")
'''

'''10

numero = input("Ingrese un numero: ")
num = int(numero)

divisores=0

for i in range(1, num, 1):
    if ((num%i) == 0):
        if(divisores==0):
            divisores=str(i)
        else:
            divisores = divisores + ", " + str(i)
        
    
print("Divisores:", divisores)
'''

'''11

numero = input("Ingrese un numero: ")
num = int(numero)

divisores=0

for i in range(1, num+1, 1):
    if ((num%i) == 0):
        divisores = divisores + 1
    
if divisores == 2:
    print("El numero ingresado es primo")
else: print("El numeroingresado NO es primo")
'''

'''12

nota = -1

while (nota<0 or nota>10):
    nota = input("Ingrese la nota: ")
    nota = float(nota)

if nota<3:
    print("Muy deficiente")

elif nota<5:
    print("Insuficiente")

elif nota<6:
    print("Suficiente")

elif nota<7:
    print("Bien")

elif nota<9:
    print("Notable")

elif nota<=10:
    print("Sobresaliente")
'''

'''13

j=30

for j in range(1, j+1, 1):
    for i in range(0,j,1) :  
        print(j, end="")
    print(" ")
    print(" ")

'''

'''14

n=int(input("Ingresa un numero: "))

for i in range(n, 0, -1):
    for j in range(1,i+1,1):
        print(i, end="")
    print(" ")
    print(" ")

'''

#15

m4=4
m9=9
l5=6

for i in range(1,501,1):
    if i==l5:
        print(" ")
        print("------------------------------------------------------------------------------------------------------")
        print(" ")
        l5=l5+5
    else:
        print(" ")

    if i==m4:
        if i ==m9:
            print(i,"(Multiplo de 4)(Multiplo de 9)")
            m4 = m4 + 4
            m9 = m9 + 9

        else: 
            print(i,"(Multiplo de 4)")
            m4 = m4 + 4

    elif i==m9:
        print(i,"(Multiplo de 9)")
        m9 = m9 + 9
    
    else:
        print(i)
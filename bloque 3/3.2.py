#Programa.2 Comparación de numeros enteros
#Elaborado el 28/10/2024
#Elaborado por : GABRIELA SILVESTRE VERA 

num1= int(input("Ingresa el numero 1:"))
num1 = int(num1)

num2 = int(input("Ingresa el numero 2:"))


if (num1 > num2):
    print(str(num1) + "\nEs mayor que " + str(num2))

elif num1 == num2:
    print(str(num1) + "\nEs igual que " + str(num2))

else:
    print(str(num1) + "\nEs menor que " + str(num2))

print("¡Gracias por usarme!")  

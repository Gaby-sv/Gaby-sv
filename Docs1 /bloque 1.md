## Programa 2.
Programa que solicita el nombre al usuario e imprime un mensaje personalizado

### Explicación del programa
En la línea 6 se solicita el nombre al usuario con la función input().

 Python
nombre = input("Nombre de usuario: ")  

La función input() permite al usuario ingresar datos desde el teclado.
El texto dentro de los paréntesis "Nombre de usuario: " se muestra como un mensaje para indicar al usuario qué ingresar.
El valor ingresado se almacena en la variable nombre.

En la línea 7 se usa print() para mostrar un mensaje personalizado con el nombre ingresado.

print("Hola", nombre, "que tengas un bonito día")

La función print() muestra en pantalla un mensaje que incluye:
El texto fijo "Hola" y "que tengas un bonito día".
El valor de la variable nombre, que contiene el nombre del usuario ingresado en la línea anterior.
Las comas permiten concatenar (unir) textos y variables dentro de la función print().

La función input nos permite ingresar datos desde el teclado y lo almacena en una variable, en este caso, la variable nombre

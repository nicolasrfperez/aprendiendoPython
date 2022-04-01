numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numAdiv=0

while numAdiv != 777:
    numAdiv = int(input("ingresa un numero: "))
    print("estas dentro del ciclo hasta q adivines")

print("adivinaste el numero secreto")

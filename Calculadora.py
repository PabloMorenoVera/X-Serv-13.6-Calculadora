#!/usr/bin/python3

#Programa para simular una calculadora
import sys

try:
    if len(sys.argv) == 4:
        if sys.argv[1] == '+':
            print(int(sys.argv[2])+int(sys.argv[3]))
        elif sys.argv[1] == '*':
            print(int(sys.argv[2])*int(sys.argv[3]))
        elif sys.argv[1] == '/':
            print(int(sys.argv[2])/int(sys.argv[3]))
        elif sys.argv[1] == '-':
            print(int(sys.argv[2])-int(sys.argv[3]))
        else:
            print('Función introducida errónea. Introduce : "+", "-", "\*", "/"')
    else:
        print('Número de argumentos incorrecto. Por favor introuzca: Nombre_Progama Función Número Número')

except ValueError:
    print('Números mal introducidos. Por favor introduzca: Nombre_Progama Función Número Número')

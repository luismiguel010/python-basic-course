
# #Función sin prámetros
# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# #Función con parámetros
# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')

#Función con return
def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)

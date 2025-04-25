#Solicita al usuario una calificación:

print("#"*40)
print("CALIFICACIÓN".center(40,"-"))
print("#"*40)

numero =-1 # SE EMPIEZA EN -1 PARA QUE EL USUARIO INGRESE UN NUMERO VALIDO.

print("======SI SU CALIFICACIÓN ES MAYOR A 60, APROBO======")

while True:
    try:
        
        numero = int(input("\nIngrese su calificación: "))

        if numero < 0: # SI EL NUMERO ES MENOR A 0 MOSTRARA UN ERROR
            print("\nNo se permiten números negativos.\nIngrese la calificación correcta.".center(40,"-"))
            continue
        
        elif numero > 100: # SI EL NUMERO ES MAYOR A 100 MOSTRARA UN ERROR
            print("\nNo se permiten números mayores a 100.\nIngrese de nuevo su calificación.".center(40,"-"))
            continue

        if numero > 59:
            print("\nUSTED APROBO".center(40,"-"))
    
        else:
            print("\nUSTED REPROBO".center(40,"-"))
    
        break

    except ValueError:
        print("\nIngrese un número válido (solo números enteros).")

# 2. CALCULAR EL PROMEDIO DE LAS CALIFICACIONES:
while True:
    try:
# PEDIR LA LISTA DE CALIFICACIONES: 
# VALIDAMOS QUE LOS NUMEROS SEAN POSITIVOS Y MENOR QUE 10

        num_calificaciones = int(input("Ingrese la cantidad de calificaciones que desea agregar a la lista: "))
        if num_calificaciones <= 0:
            print("No se permiten números negativos.\n".center(40,"-"))
            continue

        elif num_calificaciones >= 10:
            print("El maximo de calificaciones es 10.\n".center(40,"-"))
            continue

        break
    except ValueError:
        print("Ingrese un número válido. \n".center(40,"-"))  


# DIVIDIR LA LISTA:
# PEDIMOS AL USUARIO LAS CALIFICACIONES
while True:

    lista= input(f"Ingrese {num_calificaciones} calificaciones separadas por comas, (Ej: 100,89,60 ): ")

    calificaciones = lista.split(",")

    if len(calificaciones) != num_calificaciones:
        print(f"ERROR: Ingrese los valores {num_calificaciones} correspodiente.".center(40,"-"))
        continue

#CONVERTIMOS CADA NUMERO EN UN FLOAT
    try:
        calificaciones = [float(nota.strip()) for nota in calificaciones]
        break
    except ValueError:
        print("Ingrese solo números válidos. Inténtelo de nuevo.\n")
# CALCULAR EL PROMEDIO:

promedio = sum(calificaciones) / num_calificaciones

# MUESTRA DEL RESULTADO:
print("#"*40)
print(f"El promedio de las {num_calificaciones} calificaciones es: {round(promedio, 1)}".center(40,"="))
print("#"*40)

# CONTAR CALIFICACIONES MAYORES:
#RECORREMOS LA LISTA CON UN WHILE PARA VER LAS CALIFICACIONES MAYORES
while True:
    try:
        conteo = float(input("Ingrese un número para comparar: "))

        if conteo < 0:
            print("No se permiten números negativos.\nIngrese la calificación correcta.".center(40,"-"))
            continue
        
        if conteo > 100:
            print("No se permiten números mayores a 100.\nIngrese de nuevo su calificación.".center(40,"-"))
            continue

        break
    except ValueError:
        print("Ingrese un número válido.\n")

mayores = []
i = 0

while i < len(calificaciones):
    if calificaciones [i] > conteo:
        mayores.append(calificaciones[i])
    i +=1

print("#"*40)
print(f"Número ingresado: {conteo}")
print("#"*40)
print(f"Calificaciones mayores que {conteo}: {mayores}")
print("#"*40)
print(f"Cantidad de calificaciones mayores: {len(mayores)}")
print("#"*40)

# VERIFICAR Y CONTAR CALIFICACIONES ESPECÍFICAS:

# PEDIR AL USUARIO LA CALIFICACION QUE DESEA BUSCAR
while True:
    try:
        calificacion_bus = float(input("Ingrese la calificación que desea buscar: "))
        if calificacion_bus < 0 or calificacion_bus > 100:
            print("La calificación debe estar entre 0 y 100. Inténtelo de nuevo.")
            continue
        break
    except ValueError:
        print("Ingrese un número válido.")

# INICIAMOS EL CONTADOR
contador = 0  

for calificacion in calificaciones:
    if calificacion != calificacion_bus:
        continue  

    contador += 1 

    if contador != calificacion_bus: 
        print(f"La calificación {calificacion_bus} ha sido encontrada, deteniendo la búsqueda.")
        break

# Mostrar el resultado final
print(f"La calificación {calificacion_bus} aparece {contador} veces en la lista.")

#PREGUNTAR SI QUIERE CONTINUAR O SALIR

while True:
    respuesta = input("¿Desea realizar otra operación? (Sí/No): ").strip().lower()
    if respuesta in ["no", "n"]:
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    elif respuesta in ["sí", "si", "s"]:
        print("Reiniciando el programa...\n")
        break

    else:
        print("Por favor, responda 'Sí' o 'No'.")
        
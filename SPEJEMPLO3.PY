# Datos de entrada
anac = 0
aact = 0
# Datos de salida
edad = 0
# Leer datos de entrada
aact=int(input("Dame el año actual:"))
anac=int(input("Dame el año de nacimiento:"))
# Proceso
edad = aact-anac

if edad>=18:
    print(f"Tu edad es:{edad} y eres mayor de edad.")
# Datos de salida sin If
print(f"Tu edad es:{edad}.")
#ejercicio #3
print("hola mundo")

#ejercicio #4

mensaje ="hola mundo"
print(mensaje)

#ejercio #5
nombre =input ("¿Cual es tu nombre?")
print("hola",nombre)

#ejercicio #6
resultado =((3+2)/(2+5))**2
print("El resultado de la operacion es:",resultado)

#ejercicio #7
horas_trabajadas =float(input("¿Cuantas horas has trabajado?"))
costo_por_hora =float(input("¿Cual es el costo por hora trabajada?"))   
paga=horas_trabajadas*costo_por_hora
print("tu pago es:",("pago_total"))


#ejercicio #8
n=int(input("ingresa un numero entero posotivo:"))
suma = n*(n+1)/2
print(f"La suma de los primeros{n} enteros positivos es: \[{suma:.2f}\]")

#ejercicio #9
peso=float(input("ingresa tu peso en kg:"))
estatura=float(input("ingrasa tu estatura en metros:"))

kgm=peso/(estatura**2)

print(f"tu indice de Masa corporal es:")



#ejercicio #10
num_engranes = int(input("Ingrese el número de engranes vendidos: "))
num_cilindros = int(input("Ingrese el número de cilindros vendidos: "))
peso_engrane = 112  # Peso de cada engrane en gramos
peso_cilindro = 75  # Peso de cada cilindro en gramos
peso_total = (num_engranes * peso_engrane + num_cilindros * peso_cilindro) / 1000
print(f"El peso total del paquete que será enviado es: \[{peso_total:.2f} kg\]")


# ejercicio #11
precio_habitual = 3.49
num_barras_no_frescas = int(input("Ingrese el número de barras de pan vendidas que no son del día: "))
descuento = 0.6  # 60% de descuento
costo_final = (num_barras_no_frescas * precio_habitual) * (1 - descuento)

print(f"Precio habitual de una barra de pan: \[{precio_habitual:.2f} pesos\]")
print(f"Descuento por no ser fresca: \[{descuento*100:.0f}%\]")
print(f"Costo final total: \[{costo_final:.2f} pesos\]")

# ejercico #12
contraseña_guardada = "sml"
contraseña_introducida = input("Ingrese la contraseña: ")
if contraseña_introducida.lower() == contraseña_guardada.lower():
    print("La contraseña coincide.")
else:
    print("La contraseña no coincide.")


#ejercicio #13
numero1=float ("introduce el primer numero")
numero2=float("introduce el segundo numero:")
if numero2==0:
    print("error:no es posible dividir por cero")
else:
    resultado=numero1/numero2
print(f"el resultado de la division es:{resultado}")

#ejercicio #14
numero1 



#ejercicio #15
palabra = input("Ingrese una palabra: ")
for i in range(10):
    print(palabra)

#ejercicio #16
numero=int(input("introduce un numero entero positivo:"))
if numero<= 0:
    print("el numero debe ser positivo")
else:
    impares=[]
    for i in range(1,numero + 1,2):
        impares.append(str(i))
print(",".join(impares))
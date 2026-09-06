"""
mensaje = input("hola quien es?\n")
print(f"hola,{mensaje.title()} como estas?")

altura= input("cuantos cm medis?\n")
altura=int(altura)#al poner int logramos darle entender a python que vamos a pasarle un num y no un string
if altura >= 180:
    print(f"tenes {altura}cm de altura,no podes entrar")
else:
    print("tenes la altura perfecta,pasa!")

numero= input("decime un numero\n")
numero= int(numero)
if numero %2 == 0:
    print(f"el numero {numero} es par")
else:
    print("es impar")

multiplo= input("por favor escribi un numero\n")
multiplo = int (multiplo)
if multiplo % 10 == 0:
    print(f"el numero {multiplo} es multiplo de 10")
else:
    print(f"el numero {multiplo} no es multiplo de 10")    

numeroactual = 0
while numeroactual <= 5:
    print(numeroactual)
    numeroactual +=1
prompt= "\ndeci un mensaje que queres que repita"
prompt +="\npara parar escribi: shh\n"

mensaje =""
while mensaje != "shh":
    mensaje = input(prompt)
    if mensaje !="shh":
        print(mensaje)

current_number =0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue

print(current_number)                                                           


# DE ESTA MANERA PASAMOS UNA LISTA A OTRA USANDO WHILE:

unconfirmed_users=['anna','pablo','diego','alan']

confirmed_users=[]
while unconfirmed_users:
    current_users=unconfirmed_users.pop()#EN CADA VUELTA SACAMOS EL ULTIMO ELEMENTO Y LO GUARDAMOS EN CURRENT_USERS
    print(f"verificando el usuario:{current_users.title()}")
    confirmed_users.append(current_users)#EN CADA VUELTA AGARRAMOS EL ELEMENTO GUARDADO Y LO VOLVEMOS A AGUARDAR EN OTRA VARIABLE LLAMADA CONFIRMED_USERS
print("\n LOS SIGUIENTES USUARIOS FUERON CONFIRMADOS:\n")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())


#ELIMINAR CON WHILE UN DATO QUE SE REPITE:
animales=['gato','perro','pez','lagarto','gato','halcon','gato','caballo','mammut','gato']
while 'gato' in animales:
    animales.remove('gato')
print(animales)
"""
#RELLENAR UN DICCIONARIO CON LA ENTRADA DE UN USUARIO:
respuestas={}
encuesta_activa=True
while encuesta_activa:
#pide en nombre y la respuesta de la persona:
    nombre=input("\ncual es tu nombre?")
    respuesta=input("\ncual es tu montaña favorita?")
    #guardo la respuesta en el diccionario
    respuestas[nombre]=respuesta
    #preguntar si alguien mas va hacer la encuensta:
    repetir=input("te gustaria que otra persona responda? si/no\n")
    if repetir=='no':
        encuesta_activa=False
#la encuesta esta completa y muestro los resultados:
print("\nRESULTADO DE LA ENCUESTA:\n")
for name,respuesta in respuestas.items():
    print(f"{name}le gusta la montaña{respuesta}")


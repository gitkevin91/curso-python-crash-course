mensaje="hola esto es un mensaje"
print (mensaje)

nombre= "ada "
apellido= "lovelace"
nombreCompleto=f"{nombre}{apellido}"
print(f"hola,{nombreCompleto.title()}!")
prefijos="https//:www.argonauta.com.ar"
print(prefijos.removeprefix('https//:'))
nombre2="kevin"

apellido2="garcia"
fullname=f"{nombre2} {apellido2}"
print(f"hola {fullname} como estas?".upper())

nombre3="carola"
apellido3="marini"
fullname=f"{nombre3} {apellido3}"
print(f"hola {fullname.title()} como estas?")

autor="\t albert einstein"
cita="una persona que nunca cometio un error nunca hizo nada nuevo"
mensaje=(f'{autor.lstrip()}\n una vez dijo,"{cita}"').strip()
print(mensaje)
print(f'{autor} una vez dijo,"{cita}"')
filename="python_notes.txt"
print(filename.removesuffix(".txt"))
#esto es un comentario en python se usa numeral # no doble barra //
mangas = ["gantz","vagabond","gigant"]
print(mangas[0].title())
mensaje2=f"mi manga favorito siempre va ser {mangas[0].title()}"
print(mensaje2)
amigos=["leo","fede","lauti","nadia","guada"]
print(f"tengo muy buenos recuerdos con {amigos[4].title()}")
print(f"tengo muy buenos recuerdos con {amigos[3].title()}")
print(f"tengo muy buenos recuerdos con {amigos[2].title()}")
print(f"tengo muy buenos recuerdos con {amigos[1].title()}")
print(f"tengo muy buenos recuerdos con {amigos[0].title()}")
motos=["yamaha r6","d","a","g","c","b"]
amigos[3]="almendra"
amigos.append("calidoscopio")#con este metodo insertamos un elemento al final de la lista
print(amigos)
amigos.insert(0,"magui")#las comillas solo rodean el nombre en este caso por ser un string
print (amigos)
del amigos[0]#con el metodo DEL eliminamos un elemento que sepamos su indice
print (amigos)
examigos=amigos.pop()#pop se usa para eliminar el ultimo indice y a su vez guardar el valor en otra variable
print (examigos)#aca va aparecer guada ya que era el ultimo valor en la lista
print (amigos)
futuraMoto="yamaha r6"
motos.remove(futuraMoto)#de esta manera lo que hacemos es que una variable con un dato especifico que coincida con uno de la lista sea eliminado
print(f"en dos años mi moto va ser la {futuraMoto.title()}")
ciudades=["morocco","london","ibiza","new york","madrid","beijing","tokio","roma"]
print(f"  {ciudades}")


sinvisa=ciudades.pop()
print(f"no pude entrar en {sinvisa} por que no tengo visa")
ciudades.append("kioto")
print(ciudades[7])
ciudades.insert(8,"managua")
print(ciudades[8])
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")

print(f"felicidades, vas a viajar a:{ciudades[0]}")
print(f"felicidades, vas a viajar a:{ciudades[1]}")
del(ciudades)


print(sorted(motos))#el metodo sorted ordena la lista igual que sort pero de manera temporal
print(motos)
lugares=["japon","vietnam","rumania","irlanda","españa"]
print(sorted(lugares))
print(lugares)
print(sorted(lugares,reverse=True))
print(lugares)
lugares.reverse()#el metodo reverse invierte el ordenamiento del array
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)
for lugar in lugares:# por cada nombre de un lugar en lugares escribi el nombre del lugar
    print (f"{lugar.title()} es un lugar hermoso para visitar!")
    print(f"escuche que {lugar.title()} tiene muy buena gastronomia \n")# por cada elemento dentro del bucle se ejecuta todas las sentencias en el for

print ("esos son los paises que voy a visitar!\n")#la falta de sangria marca el fin del bucle

mascotas=["perro","gato","pez","hamster"]

for mascota in mascotas:
    print(f"el{mascota.title()} es una excelente mascota")
    print("ademas es buena compania\n")
print("todas son buenas mascotas")

numeros=[1,2,3,4,5,6]
for numeros in range(1,7): #in rage usa dos argumentos el primero desde donde tiene que empezar y el segundo es hasta donde tiene que mostrar el cual siempre va ser uno anterior no olvidar el :
    print(numeros)
numeros=list(range(1,6))#con list podemos ordenar en forma de lista un array de numeros
print(numeros)    
lista_numeros=list(range(2,11,2))#el tercer argumento se usa para decirle cuantos numeros se tiene que saltar

print(lista_numeros)
cuadrado=[]#inicio un array vacio
for valor in range(1,11): #creo un for con variable (temporal) "valor" con un rango de 1 hasta 10
    cuadrados=valor ** 2#creo la variable cuadrados y le asigno el valor de su vuelta elevado a la 2=1*1=1,2*2=4 etc
    cuadrado.append(cuadrados)#con append agrego los resultados a la variable cuadrado que estaba vacia
print (cuadrado)#imprimo los resultados
# PODEMOS USAR LOS METODOS: SUM()PARA QUE NOS DEVUELVA EL NUMERO DE MAXIMO VALOR
# PODEMOS USAR MIN() PARA QUE NOS DEVUELVA EL MENOR VALOR
# O PODEMOS USAR SUM() PARA QUE NOS DEVUELVA EL VALOR SUMADO DE TODOS LOS NUMEROS EN EL ARRAY
# A CONTINUACION EL AUTOR DEL LIBRO NOS MUESTRA COMO SERIA EL MISMO CODIGO PERO EN UNA LINEA DE COMPRECION:
squares=[value**2 for value in range(1,11)]
print (squares)

contador=[]
for num in range(1,21):#contar hasta 20
    print(num)

millon=list(range(1,1000000))#crea una lista de uno al millon


print(min(millon))
print(max(millon))

mensaje="hola esto es un mensaje"
print (mensaje)

nombre= "ada "
apellido= "lovelace"
nombreCompleto=f"{nombre}{apellido}"
print(f"hola,{nombreCompleto.title()}!")
prefijos="https//:www.argonauta.com.ar"
print(prefijos.removeprefix('https//:'))
nombre2="kevin"

apellido2="garcia"
fullname=f"{nombre2} {apellido2}"
print(f"hola {fullname} como estas?".upper())

nombre3="carola"
apellido3="marini"
fullname=f"{nombre3} {apellido3}"
print(f"hola {fullname.title()} como estas?")

autor="\t albert einstein"
cita="una persona que nunca cometio un error nunca hizo nada nuevo"
mensaje=(f'{autor.lstrip()}\n una vez dijo,"{cita}"').strip()
print(mensaje)
print(f'{autor} una vez dijo,"{cita}"')
filename="python_notes.txt"
print(filename.removesuffix(".txt"))
#esto es un comentario en python se usa numeral # no doble barra //
mangas = ["gantz","vagabond","gigant"]
print(mangas[0].title())
mensaje2=f"mi manga favorito siempre va ser {mangas[0].title()}"
print(mensaje2)
amigos=["leo","fede","lauti","nadia","guada"]
print(f"tengo muy buenos recuerdos con {amigos[4].title()}")
print(f"tengo muy buenos recuerdos con {amigos[3].title()}")
print(f"tengo muy buenos recuerdos con {amigos[2].title()}")
print(f"tengo muy buenos recuerdos con {amigos[1].title()}")
print(f"tengo muy buenos recuerdos con {amigos[0].title()}")
motos=["yamaha r6","d","a","g","c","b"]
amigos[3]="almendra"
amigos.append("calidoscopio")#con este metodo insertamos un elemento al final de la lista
print(amigos)
amigos.insert(0,"magui")#las comillas solo rodean el nombre en este caso por ser un string
print (amigos)
del amigos[0]#con el metodo DEL eliminamos un elemento que sepamos su indice
print (amigos)
examigos=amigos.pop()#pop se usa para eliminar el ultimo indice y a su vez guardar el valor en otra variable
print (examigos)#aca va aparecer guada ya que era el ultimo valor en la lista
print (amigos)
futuraMoto="yamaha r6"
motos.remove(futuraMoto)#de esta manera lo que hacemos es que una variable con un dato especifico que coincida con uno de la lista sea eliminado
print(f"en dos años mi moto va ser la {futuraMoto.title()}")
ciudades=["morocco","london","ibiza","new york","madrid","beijing","tokio","roma"]
print(f"  {ciudades}")


sinvisa=ciudades.pop()
print(f"no pude entrar en {sinvisa} por que no tengo visa")
ciudades.append("kioto")
print(ciudades[7])
ciudades.insert(8,"managua")
print(ciudades[8])
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")
sinvisa=ciudades.pop()
print(f"no voy a poder ir a{sinvisa}")

print(f"felicidades, vas a viajar a:{ciudades[0]}")
print(f"felicidades, vas a viajar a:{ciudades[1]}")
del(ciudades)


print(sorted(motos))#el metodo sorted ordena la lista igual que sort pero de manera temporal
print(motos)
lugares=["japon","vietnam","rumania","irlanda","españa"]
print(sorted(lugares))
print(lugares)
print(sorted(lugares,reverse=True))
print(lugares)
lugares.reverse()#el metodo reverse invierte el ordenamiento del array
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)
for lugar in lugares:# por cada nombre de un lugar en lugares escribi el nombre del lugar
    print (f"{lugar.title()} es un lugar hermoso para visitar!")
    print(f"escuche que {lugar.title()} tiene muy buena gastronomia \n")# por cada elemento dentro del bucle se ejecuta todas las sentencias en el for

print ("esos son los paises que voy a visitar!\n")#la falta de sangria marca el fin del bucle

mascotas=["perro","gato","pez","hamster"]

for mascota in mascotas:
    print(f"el{mascota.title()} es una excelente mascota")
    print("ademas es buena compania\n")
print("todas son buenas mascotas")

numeros=[1,2,3,4,5,6]
for numeros in range(1,7): #in rage usa dos argumentos el primero desde donde tiene que empezar y el segundo es hasta donde tiene que mostrar el cual siempre va ser uno anterior no olvidar el :
    print(numeros)
numeros=list(range(1,6))#con list podemos ordenar en forma de lista un array de numeros
print(numeros)    
lista_numeros=list(range(2,11,2))#el tercer argumento se usa para decirle cuantos numeros se tiene que saltar

print(lista_numeros)
cuadrado=[]#inicio un array vacio
for valor in range(1,11): #creo un for con variable (temporal) "valor" con un rango de 1 hasta 10
    cuadrados=valor ** 2#creo la variable cuadrados y le asigno el valor de su vuelta elevado a la 2=1*1=1,2*2=4 etc
    cuadrado.append(cuadrados)#con append agrego los resultados a la variable cuadrado que estaba vacia
print (cuadrado)#imprimo los resultados
# PODEMOS USAR LOS METODOS: SUM()PARA QUE NOS DEVUELVA EL NUMERO DE MAXIMO VALOR
# PODEMOS USAR MIN() PARA QUE NOS DEVUELVA EL MENOR VALOR
# O PODEMOS USAR SUM() PARA QUE NOS DEVUELVA EL VALOR SUMADO DE TODOS LOS NUMEROS EN EL ARRAY
# A CONTINUACION EL AUTOR DEL LIBRO NOS MUESTRA COMO SERIA EL MISMO CODIGO PERO EN UNA LINEA DE COMPRECION:
squares=[value**2 for value in range(1,11)]
print (squares)


for num in range(1,21):#contar hasta 20
    print(num)

millon=list(range(1,1000001))#crea una lista de uno al millon


print(min(millon))#muestro el menor valor
print(max(millon))#muestro el mayor valor
print(sum(millon)) #muestro la suma de todos los numeros

multiplos=list(range(3,30,3))#lista que muestra los multiplos de 3
print(multiplos)

cubo=[]#lista de numeros elevado a la 3
for cub in range(1,10):#inicio bucle con variable temporal con 10 vueltas
    resulcubo=cub**3 #variable temporal que con cada vuelta guarda el valor elevado a la 3
    cubo.append(resulcubo) #guardo el valor de resulcubo en variable cubo
    print(cubo)#imprimo

cubito=[cubit**3 for cubit in range(1,10)]# el mismo codigo de arriba pero hecha compresion
print(cubito)

jugadores=["miguel","altor","dulcinea","patroco","leon"]
print(jugadores[0:3]) #poniendo los corchetes podemos delimitar los datos que queremos
#en este caso seria miguel,altor y dulcinea.
#podemos delimitar los trozo que queramos por ej:[-3:]se usaria para optener los 3 ultimos datos

print("aca estan mis primeros jugadores:\n")
for jugador in jugadores [:3]: # de esta manera recorremos con un for solo los 3 primeros datos
    print(jugador.title())

misComidas=["sushi","milanesas","chocolates","kiwi","yogurth"]
comidaAmigo=misComidas[:]#[:]significa que quiero todo en el array de esta manera copiamos un array si no usamos [:] simplemente el programa asigna el valor de uno al otro y si agregamos diferentes elementos ambas compartirian la informacion,por ejemplo si pongo que miscomidas.append("hamburgesa") ambas listas la tendrian
print("mis comidas favoritas son:\n")
misComidas.append("hamburguesas")
print(misComidas)
print("\nlas comidas favoritas de mi amigo son:\n")
comidaAmigo.append("ravioles")
print(comidaAmigo)

#esto es una tupla(una lista inmutable):
menu=("pollo","spagetti","asado","burritos")

for comidas in menu:#para recorrer una tupla no hace falta poner de donde a donde ejm:[1,3]
    print(comidas)

menu=("pollo","strudel","asado","sashimi")#tupla modificada con nuevos valores
for nuevomenu in menu:
    print(nuevomenu)
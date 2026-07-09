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
mensaje="hola esto es un mensaje"
print (mensaje)

nombre= "ada "
apellido= "lovelace"
nombreCompleto=f"{nombre}{apellido}"
print(f"hola,{nombreCompleto.title()}!")
prefijos="https//:www.argonauta.com.ar"
prefijos.removeprefix('https//:')
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
motos=["yamaha r6","d"]
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
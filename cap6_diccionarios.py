alien_0 = {'color' : 'verde','puntos' : 100} #los diccionarios sirven para almacenar info de forma mas amplia,son colecciones de  de pares, clave:valor
print (alien_0['color'])
print(alien_0['puntos'])

#se puede añadir mas pares al diccionario:
alien_0['posicion_x'] = 25
alien_0['posicion_y'] = 0
print(alien_0)

alien_1 = {}
alien_1['color'] = 'azul'
alien_1['posicion_y'] = 1
print(alien_1)

alien_0['color'] = 'amarillo' #asi tan facil le cambiamos un valor al diccionario
print (alien_0['color'] ) 

alien_0['velocidad'] = 'medium'

if alien_0['velocidad']== 'slow':
    x_increment = 1
elif alien_0['velocidad'] == 'medium':
    x_increment = 2
else:
    x_increment = 3    
#ahora sumamos su antigua velocidad a la nueva:
alien_0['posicion_x'] = alien_0['posicion_x'] + x_increment
print(alien_0)
print(f"la nueva posicion es: {alien_0['posicion_x']}")

lenguajes_favoritos = {
    'sara':'python',
    'jen' : 'c',
    'edward' :'python',
    'phil' : 'rust',
}
lenguaje = lenguajes_favoritos['sara'].title()
print (f"El lenguaje de programacion favorito de sara es {lenguaje}")
#print(lenguajes_favoritos['miguel']) esto da error ya que no existe el par miguel por eso para evitar este tipo de errores se usa el metodo get() para usar get tenemos que asignarle una clave como primer argumento,y como segundo argumento opcional podemos pasarle un valor opcional si la clave no existe
del alien_0['puntos']# con del podemos eliminar claves/valor en este caso eliminamos los puntos
valor_de_puntos = alien_0.get('puntos','no hay puntos asignados')
print(valor_de_puntos)
persona = {
    'nombre':'carola',
    'apellido':'marini',
    'edad': 30,
    'ocupacion':'programadora',
    'hobbies':'senderismo'
    }
print(persona)
favorite_numbers ={'carola':16,'guada':17,'leon':12,'keykey':22}
print(favorite_numbers['carola'])
print(favorite_numbers['keykey'])
print(favorite_numbers['guada'])
print(favorite_numbers['leon'])

for llave,valor in persona.items():
    print(f"\nllave: {llave}")
    print(f"Valor:{valor}")

    for nombres in favorite_numbers.keys():#con keys() devuelve solo la clave
        print(nombres)

amigos = ['sara','phil']
for names in lenguajes_favoritos:
    print(f"hola! {names.title()}.")

    if names in amigos:
        lenguaje = lenguajes_favoritos[names].title()
        print(f"\t{names.title()},veo que te gusta {lenguaje}!")

if 'erin' not in lenguajes_favoritos.keys():
    print("erin,por favor decime tu lenguaje favorito!")

for name in sorted(lenguajes_favoritos.keys()):
    print(f"{name.title()},gracias por decirme tu lenguaje fav!")

for name in sorted(lenguajes_favoritos,key=len):
    print(name)

print("los lenguajes que conocemos son:") 
for lenguajes in lenguajes_favoritos.values():
   
    print(lenguajes.title())    


for lenguajes in set(lenguajes_favoritos.values()):
    print(lenguajes)
    #nota: se pueden crear conjuntos directamente usando llaves {}
    #lenguajes={'python','c','rust','python'}
    #lenguajes{'pyhon','c','rust'} cuando veamos llaves y no conjunto clave/valor no es una libreria sino un conjunto

#ejemplo de anidacion:
alien_2={'color':'blue','puntos':20}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#hacer una flota de nuevos aliens:
alienss=[]
for nuevos_aliens in range(30):
    nuevo_alien={'color':'verde','puntos':5,'velocidad':'lento'}
    alienss.append(nuevo_alien)

#print(f"la cantidad de aliens creados es de: {len(alienss)}")
for alien in alienss[:3]:
    if alien ['color']=='verde':
        alien['color']="amarillo"
        alien['velocidad']='medium'
        alien['puntos'] = 10
    elif alien['color']=='amarillo':
        alien['color']="rojo"
        alien['velocidad']='fast'
        alien['puntos'] = 15
for alien in alienss[:5]:
    print(alien)
    print("...")


pizza={
   'costra':'dura',
   'toppings':['extra queso','hongos']
}
print(f"ordenaste un {pizza['costra']}-crust pizza con los siguientes toppings:")
for toppings in pizza['toppings']:
    print(f"\t" + toppings)

favorite_lenguaje={
    'jen':['pithon','rust'],
    'sarah':['c'],
    'edwart':['rust','go'],
    'phil':['python','haskell']
}
for name,lenguajes in favorite_lenguaje.items():
    print(f"\n el lenguaje favorito de{name.title()}es:")
    for lenguaje in lenguajes:
        print(f"\t{lenguaje.title()}")




"""
def greater_user(username):
    print (f'hello {username.title()}')

greater_user('kevin')
 
def describe_mascota(tipodeanimal,nombre_animal):
    print(f"mi pet is a {tipodeanimal.title()}")
    print(f"mi {tipodeanimal.title()} se llama {nombre_animal.title()}\n") 

describe_mascota('hamster','william')
describe_mascota('perro','pepe')

#funcion para retornar un valor apartir de dos argumentos y usarlo para completar un
def nombre_completo(nombre,apellido):
    nombrecompleto=f"{nombre}, {apellido}"
    return nombrecompleto.title()
musico=nombre_completo('jimmy','hendrix')
print(musico)

#si quiero que tenga un parametro opcional lo que podria hacer es rellenarlo con un espacio en blanco

def nombre_completo(nombre,apellido,nombremedio=''):
    if nombremedio:
        nombre_completo=f"{nombre} {nombremedio} {apellido}"
    else:
        nombre_completo=f"{nombre} {apellido}"
    return nombre_completo.title()

musico = nombre_completo('jimmi','hendrix')
print(musico)
musico = nombre_completo('john','hooker','lee')

print (musico)

#tambien podriamos devolver un diccionario:
def nombre_completo(nombre,apellido):
    persona={'first':nombre,'last':apellido}
    return persona
musico=nombre_completo('gustavo','cerati')
print(musico)


def get_formated_name(firs_name,last_name ):
    full_name=f"{firs_name} {last_name}"
    return full_name.title()

while True:
    print("decime tu nombre completo")
    print("\napreta q para salir")
    f_name=input("nombre?\n")
    if f_name =="q":
        break

    l_name=input("apellido?")
    if l_name =="q":
        break
    nombre_completo = get_formated_name(f_name,l_name)
    print(f"\n Hola {nombre_completo} como estas?")


#funcion que recorre una lista y devuelve un saludo personalizado para cada integrante:
def grate_users(names):
    "imprime un saludo sencillo para cada nombre de la lista"
    for name in names:
        mensaje=f"hola {name.title()} como estas?\n"
        print(mensaje)
user_names=['pedro','jeronimo','papanicolao']
grate_users(user_names)

#modificar una lista en una funcion:


def print_models (modelos_noimpresos,modelos_impresos):
    while modelos_noimpresos:
        modelos_actuales=modelos_noimpresos.pop()
        print(f"se acaba de imprimir el modelo: {modelos_actuales}")
        modelos_impresos.append(modelos_actuales)

def mostrar_impresos(modelos_impresos):
    print ("modelos que fueron impresos:")
    for modelos in modelos_impresos:
       print(modelos)

modelos_noimpresos=['robot','muñeca','engranaje']
modelos_impresos=[]

print_models(modelos_noimpresos,modelos_impresos)
mostrar_impresos(modelos_impresos)

#como evitar que una funcion modifique una lista:
def print_models (modelos_noimpresos,modelos_impresos):
    while modelos_noimpresos:
        modelos_actuales=modelos_noimpresos.pop()
        print(f"se acaba de imprimir el modelo: {modelos_actuales}")
        modelos_impresos.append(modelos_actuales)

def mostrar_impresos(modelos_impresos):
    print ("modelos que fueron impresos:")
    for modelos in modelos_impresos:
       print(modelos)

modelos_noimpresos=['robot','muñeca','engranaje']
modelos_impresos=[]

print_models(modelos_noimpresos[:],modelos_impresos)
mostrar_impresos(modelos_impresos)




#pasar un numero arbitrario de argumentos:
def make_pizza (*toppings):
    #imprime la lista de ingredientes solicitados
    print(f"haciendo una pizza con los siguientes ingredientes:")
    for toppings in toppings:
        print(f"- {toppings}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra chease')


#mezclar argumentos posicionales y arbitrarios
def make_pizza(size,*toppings):
    print(f"haciendo una pizza de tamaño:{size} con los siguientes toppings:")
    for toppings in toppings:
        print(f"-{toppings}")
make_pizza(16,'pepperoni')
make_pizza(18,'mushrooms','green pepers','extra cheese','tomato','extra tomato sauce')
#usar argumentos de palabra clave arbitrarios:
 
def build_profile(first,last,**user_info):
    #crea un diccionario con todo lo que sabemos del usuario.
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile = build_profile('albert','einstein',location ='princeton',fiel ='physics')
print(user_profile)
 """

def make_pizza(size,*toppings):
    #resume la pizza que estamos apunto de hacer.
    print(f"vamos a hacer una pizza de tamaño:{size} con los siguientes toppings:\n")  
    for toppings in toppings:
        print(f"-{toppings}")     
# ahora hacemos el archivo indepentendiente llamado make_pizza.py en el mismo direcctorio que pizza.py
make_pizza.py
import pizza
pizza.make_pizza(16,'pepperoni')   
pizza.make_piza(20,'muzzarella','tomate','albahca')   
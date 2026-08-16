 # capitulo 5
cars =['audi','bmw','suzuki','toyota']

for car in cars:
    if(car =='bmw'):
        print (car.upper())
    else:
        print(car.title())    

ep=1
cap=2
if ep==1 and cap==2:
    print("el and funciono bien")
  
if ep==1 or cap==33:
    print ("el or tambien funciono")

baneados=["sara","lola","ailu"]
usuario="caro"
observados=[usuario]
if"sara" in baneados:
      print("estas baneada")


if usuario not in baneados:
    print(f"{usuario.title()},no estas baneada")

    if usuario in observados:
         print("te estamos vigilando")
elif usuario == "caro" or baneados[0]=="sara":
    print("hola caro")
 
    
else:
    print("estas baneada ") 

ingredientes_requeridos=['tomate','queso','cebolla','pepino','hongos']

if "tomate"in ingredientes_requeridos:
    print("verdadero")

if 'papa' not in ingredientes_requeridos:
    print("aca no hay papa")

auto = 'ferrari'
print (auto == 'ferrari')

cosas= ['fotos','vasos','platos','celular']
if 'fotos' in cosas:
    print(True)
if 'regla' not in cosas:
    print(False)

largo='FOTOS'
if largo.lower() == cosas[0]:
    print('esta aca')

if largo == cosas[0]:
    print('esta aca')
else:
    print("no esta aca")

for ingrediente in ingredientes_requeridos:
    if ingrediente =='hongos':
        print("no tenemos hongos")
    else:
        print(f"añadiendo {ingrediente} a la pizza")        

lista_vacia=[]
if lista_vacia:#de esta manera se puede comprobar si la lista tiene elementos o no
    print("la lista tiene elementos")#el if se ejecuta si la lista tiene elementos
else:#el else se ejecuta si la lista esta vacia
    print("la lista está vacía")
#usar multiples listas en un for
condimentos=['tomate','cebolla','ketchup','hongos']
for extra in ingredientes_requeridos:
    if condimentos in ingredientes_requeridos:
        print(f"añadiendo {condimentos} a la pizza")
    else:
        print(f"no tenemos {condimentos} disponible en este momento") 

avariable_toppings=['queso','tomate','peperoni','salsa','anana']
request_toppings=['tomate','papas fritas','queso','salsa']

for request_toppings in request_toppings:

     if request_toppings in avariable_toppings:
         print(f"agregando {request_toppings}")
     else:
        print(f"no nos queda{request_toppings}")     
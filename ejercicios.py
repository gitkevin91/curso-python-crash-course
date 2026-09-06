"""
def hacer_camisas(talle):
#8-3 funciones
    print(f"el talle de la camisa es:{talle}")
hacer_camisas(44)

#8-3
def nombre_ciudad (ciudad,pais):
    lugar=f"{ciudad},{pais}"
    return lugar
while True:
    print("indicanos en que lugar estas:\n")
    print("para salir apreta q ")

    c_lugar=input("nombre de la ciudad?")
    if c_lugar =="q":
        break
    p_lugar=input("\nnombre del pais?")
    if p_lugar =="q":
        break
    ciudad_pais=nombre_ciudad(c_lugar,p_lugar).title()
    print(ciudad_pais)
    
#funciones: 8-12
def sanguches(*ingredientes):
    print("los ingredientes seleccionados son:")
    for ingredientes in ingredientes:
        print(f"\n-{ingredientes}")

sanguches('jamon','queso','tomate','milanesa','pepino')
sanguches('carne','lechuga','tomate') 
"""
#funciones 8-13
def usuario(first,last,**info_user):
    info_user['first_name']=first
    info_user['last_name']=last
    return info_user
perfil=usuario('kevin','garcia',programador='python',residencia='islandia')
print(perfil)
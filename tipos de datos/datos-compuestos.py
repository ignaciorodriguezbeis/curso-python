lista = ["soy nacho","soy ignacio",True,1.85]  #se puede modificar

tupla = ("soy nacho","soy ignacio",True,1.85)  #no se puede modificar

lista[3] = "maquina" #esto es valido

#tupla[3] = "maquina" #esto no es valido

#print(tupla[3])

#print(lista[3])

# creado un conjunto (set) no se puede acceder a elementos por indice, no almacena datos duplicados 
conjunto = {"soy nacho","soy ignacio",True,1.85}

#conjunto ={"jajajaja te jodi"}

#print(conjunto)
diccionario = {
    'nombre' : "ignacio",
    'primer apellido' : "rodriguez",
    'segundo apellido' : "beistegui",
    'apodo' : "nacho",
    'altura' : 1.72,
    'peso' : 92,
    'vivo' : True
}

print(diccionario['nombre'])


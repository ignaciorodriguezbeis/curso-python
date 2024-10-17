# Métodos de Diccionario

diccionario = {"nombre": "ignacio", "edad": 27, "ciudad": "cordoba"}

# get(): Obtiene el valor asociado a una clave, devuelve None si la clave no existe
print(diccionario.get("nombre"))  # "ignacio"
print(diccionario.get("altura"))  # None

# keys(): Devuelve una lista con todas las claves del diccionario
print(diccionario.keys())  # ["nombre", "edad", "ciudad"]

# clear(): Elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)  # {}

# pop(): Elimina y devuelve el valor asociado a una clave específica
valor_eliminado = diccionario.pop("edad")
print(valor_eliminado)  # 27
print(diccionario)  # {"nombre": "ignacio", "ciudad": "cordoba"}

# items(): Devuelve una lista de tuplas (clave, valor) de todos los elementos del diccionario
print(diccionario.items())  # [("nombre", "ignacio"), ("ciudad", "cordoba")]
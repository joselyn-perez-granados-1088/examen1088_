print("examen tienda de mascotas minino")
class josy1088: #examen♥
    nombre=0
    productos=0
    direccion=0
    idproveedor=0
    numtel=0
    frecuencia=0
    pagos=0
    def mi_lista(self):
        lista_proveedores1088=["pedigree","dogchow","whiskas","happydog","woof"]
        for x in lista_proveedores1088:
            print(x)

    def mi_tupla(self):
        tupla_productos=("comida de perro","comida de gato","jaulas","ropa","arnes")
        for x in tupla_productos:
            print(x)

    def mi_diccionario(self):
        diccionario_direccion={
            "dogchow: ":"higo 7045 el granjero",

            "pedigree: ":"oasis 9754 praderas",

            "whiskas: ":"oasis 9639 praderas",

            "happydog: ":"calle tornillo 3408",

            "woof: ":"oasis de ghaba 1208"
                                }
        for x,y in diccionario_direccion.items():
            print(x,y)
#objeto para atributos
joselyn=josy1088 #joselyn representa el objeto proveedor
#mostrar datos 
datos=josy1088()
print(" ")
print("listado de proveedores")
print(" ")
datos.mi_lista()
print(" ")

print("tupla de edad de perros")
print(" ")
datos.mi_tupla()
print(" ")

print("diccionario de raza de perros")
print(" ")
datos.mi_diccionario()

joselyn.nombre="pedigree"
joselyn.productos="comida 24kilos"
joselyn.direccion="calle higo 7045"
joselyn.idproveedor=1234
joselyn.numtel=6567727342
joselyn.frecuencia="baja"
joselyn.pagos=5
print(" ")
print("atributos del proveedor")
print(" ")
print(f"edad: {joselyn.nombre}")
print(f"genero: {joselyn.productos}")
print(f"pelo: {joselyn.direccion}")
print(f"estatura: {joselyn.idproveedor}")
print(f"peso: {joselyn.numtel}")
print(f"estatura: {joselyn.frecuencia}")
print(f"peso: {joselyn.pagos}")
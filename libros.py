from datos import libros ,prestamos
def mostrar_libros():
    print("Lista de libros Disponibles: ")
    for libro  in libros:
        estado ="disponible" if libro['disponible'] else "prestado"
        print(f"{libro['nombre']} - {libro['autor']} - {estado}")

def prestar_libro(usuario):
    mostrar_libros()
    titulo = input("ingrese el titulo del libro a prestar: ")
    for libro in libros:
        if libro["nombre"]==titulo and libro["disponible"]:
            libro["disponible"]=False
            prestamos.append({"usuario":usuario,"libro":titulo})
            print("Libro prestado correctamente")
            return
    print("Libro no disponible")
    
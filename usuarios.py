from datos import usuarios

def registrar_usuario():
    nombre = input("ingrese el nombre del usuario: ")
    contrasena = input("ingrese la contrasena del usuario: ")
    usuarios.append({"nombre": nombre, "contrasena": contrasena})
    print("Usuario registrado correctamente")
def login ():
    nombre = input("ingrese el usuario: ")
    contrasena = input("ingrese la contrasena: ")
    for usuario in usuarios :
        if usuario["nombre"]==nombre and usuario["contraña"]==contrasena:
            print("BLogin Exitoso")
            return nombre
    print("Usuario o contrasena incorrectos")
    return None
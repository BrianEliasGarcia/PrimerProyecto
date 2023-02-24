import json

def listar_usuarios():
    with open("guardadouser.txt", 'r') as f:
        lectura = f.read()
        users = json.loads(lectura)
        return users

def registrar_usuario():
    file = open("guardadouser.txt")
    file.close()
    users_in_file = listar_usuarios()
    flag = True
    username = input('Introduzca su usuario: ')
    for user in users_in_file:
        if user['username'].lower() == username.lower():
            flag = False
    if flag:
        with open("guardadouser.txt", 'a') as f:
            password = input('Introduzca su password: ')
            users_in_file.append({"username":username, "password":password})
            json.dump(users_in_file, f)
    else:
        print("Ese usuario ya existe \n")

2
def login():
    users_in_file = listar_usuarios()
    username = input('Introduzca su usuario: ')
    flag = False
    for user in users_in_file:
        if user['username'].lower() == username.lower():
            flag = True
    if not flag:
        return False, "No existe el usuario que ingreso"
    else:
        for i, p in enumerate(users_in_file):
            if p['username'] == username:
                index = i
        password = input('Ingrese su contraseña: ')
        if users_in_file[index]['password'] == password:
            return True, 'Login Succesfully'
        else:
            return False, 'Contraseña incorrecta, inténtalo de nuevo'

while True:
    opcion = input('''
    Ingrese su opcion
    1. Listar Usuarios
    2. Agregar Usuario
    3. Login
    4. Exit
    ''')

    if opcion == '1':
        print(listar_usuarios())
    elif opcion == '2':
        registrar_usuario()
    elif opcion == '3':
        while True:
            a, b = login()
            if a:
                print(b)
                break
            else:
                print(b)
    else:
        break

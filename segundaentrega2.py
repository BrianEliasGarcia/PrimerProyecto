from random import randint


class Cliente:
    def __init__(self, nombre, dni, telefono, direccionEntrega, email):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.direccion_entrega = direccionEntrega
        self.email = email
        self.pago = None
        self.numero_cliente = None
        self.envio = None
        self.titulo_libro = None
        self.formato = None

    def libro(self):
        self.formato = input(
            "Ingrese en que formato desea comprar Fisico (1) o Digital (2): ")
        self.titulo_libro = input("Ingrese el nombre del Libro: ")

    def medios_de_pago(self):
        self.pago = input("Usted paga en efectivo o tarjeta: ")
        if self.formato == 1:
            self.envio = "El Envio demora 72 horas habiles."
        else:
            self.envio = "Su Libro llegara en PDF a su Correo Electronico."
        self.numero_cliente = randint(1000000, 9999999)

    def __str__(self):
        return f"""
        El nombre del Cliente es: {self.nombre}\n
        El DNi es: {self.dni}\n
        El telefono es: {self.telefono}\n
        La direccion de entrega es: {self.direccion_entrega}\n
        Su factura sera enviada a : {self.email}\n
        El formato ingresado es: {self.formato}\n
        El Libro es: {self.titulo_libro}\n
        Metodo de pago elegido: {self.pago}\n
        {self.envio}\n
        Su NÂ° de cliente es: {self.numero_cliente}\n"""


FLAG = True
while FLAG:
    opcion = int(input("""
        Bienvenido al programa.
        Ingrese que quiere hacer.
        1. Ingresar un cliente nuevo
        2. Cerrar programa.
    """))
    if opcion == 1:
        nombre = input("Ingrese Nombre y Apellido: ")
        dni = input("Ingrese un DNI: ")
        telefono = input("Ingrese un Telefono: ")
        direccionEntrega = input("Ingrese la direccion de entrega del producto: ")
        email = input("Ingrese un correo electronico: ")
        email_comprobacion = input("Reingresar el correo electronico: ")
        if email_comprobacion == email:
            p1 = Cliente(nombre, dni, telefono, direccionEntrega, email)
            p1.libro()
            p1.medios_de_pago()
            print(p1)
        else:
            print('Los email no coinciden. Intentelo denuevo')
    else:
        print('Cerrando programa...')
        break
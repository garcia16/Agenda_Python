class Persona:
    """Esta es la clase Padre que contendra 4 atributos y 2 metodos los heredaran las clases
     Familiares y Amigos """
    def __init__(self):
        self.nombre=' '
        self.apellido=' '
        self.telefono=' '
        self.ciudad=' '
    def __str__(self):
        return 'nombre: '+self.nombre+' '+'apellidos: '+self.apellido+' '+'telefono: '+self.telefono+' '+'ciudad: '+self.ciudad
class Amigo(Persona):
    """Hereda de Persona y tendra una lista que se rellenera con objetos de esta clase"""

    def __init__(self):
        super().__init__()
        self.afinidad=' '

    def __str__(self):
        return super().__str__()+' '+'afinidad: '+self.afinidad

lista_amigos=[]#creo una lista que va a ser global para la clase amigo

class Familiar(Persona):
    """Hereda de Persona y tendra una lista que se rellenera con objetos de esta clase"""

    def __init__(self):
        super().__init__()
        self.parentesco = ' '

    def __str__(self):
        return super().__str__() + ' ' + 'parentesco: ' + self.parentesco


lista_familiar=[]#creo una lista que va a ser global para la clase familiar

def InsertarAmigo():
    """Este metodo servira para rellenar la lista de amigos,
     creo un objeto de la clase amigos y le añado mediante input los datos"""
    amigo = Amigo()
    amigo.nombre = input('escribe el nombre')
    amigo.apellido = input('escribe el apellido')
    amigo.ciudad = input('escribe la ciudad')
    amigo.telefono = input('escribe el telefono')
    amigo.afinidad = input('escribe la afinidad')
    lista_amigos.append(amigo)
def InsertarFamiliar():
    """Este metodo servira para rellenar la lista de familaires,
     creo un objeto de la clase familiar y le añado mediante input los datos"""
    familia = Familiar()
    familia.nombre = input('escribe el nombre')
    familia.apellido = input('escribe el apellido')
    familia.ciudad = input('escribe la ciudad')
    familia.telefono = input('escribe el telefono')
    familia.parentesco = input('escribe el parentesco')
    lista_familiar.append(familia)
def VerAmigo():
    """Este metodo nos permitira ver los amigos añadidos gracias el metodo __str__"""
    for i in lista_amigos:
        print(i.__str__())
def VerFamiliar():
    """Este metodo nos permitira ver los familiares añadidos gracias el metodo __str__"""
    for i in lista_familiar:
        print(i.__str__())
def ModificarAmigo():
    """Este metodo nos permitira modificar el amigo que tenga el telefono que ingresemos por teclado"""
    a = input('ingresa el telefono del amigo que desees modificar')
    for i in lista_amigos:
        if a == i.telefono:
            i.nombre = input('ingresa el nuevo nombre')
def ModificarFamiliar():
    """Este metodo nos permitira modificar el familiar que tenga el telefono que ingresemos por teclado"""
    a = input('ingresa el telefono del familiar que desees modificar')
    for i in lista_familiar:
        if a == i.telefono:
            i.nombre = input('ingresa el nuevo nombre')
def GuardarFichero():
    """Este metodo escribira los datos de las listas en un fichero de texto """
    fichero=open("AgendaContactos.txt","wt")
    fichero.write("AMIGOS")
    for i in lista_amigos:
        fichero.write(i.__str__()+"\n")
    fichero.write("FAMILIARES")
    for i in lista_familiar:
        fichero.write(i.__str__()+"\n")

    fichero.close()
def GuardarBaseDatos():
    """Este metodo ingresa las listas de las clases en una base de datos SQlite """
    import sqlite3
    conector=sqlite3.connect("AgendaContactos.db")
    cursor = conector.cursor()
    for i in lista_amigos:
        cursor.execute("insert into AMIGOS values (?,?,?,?,?)",(i.nombre,i.apellido,i.telefono,i.ciudad,i.afinidad))
    for i in lista_familiar:
        cursor.execute("insert into FAMILIARES values (?,?,?,?,?)", (i.nombre,i.apellido,i.telefono,i.ciudad,i.parentesco))
    conector.commit()
    conector.close()
def CargarBaseDatos():
    """Este metodo se encargara de rellenar las listas mediante una consulta con los datos que hay ingresados en la base de datos"""
    import sqlite3
    conector = sqlite3.connect("AgendaContactos.db")
    cursor = conector.cursor()
    cursor1= conector.cursor()
    cursor.execute("select * from AMIGOS")
    datos = cursor.fetchall()
    for amigos in datos:
        amigo=Amigo()
        amigo.nombre=amigos[0]
        amigo.apellido = amigos[1]
        amigo.telefono = amigos[2]
        amigo.ciudad = amigos[3]
        amigo.afinidad=amigos[4]
        lista_amigos.append(amigo)
    cursor1.execute("select * from FAMILIARES")
    datos1 = cursor1.fetchall()
    for familiares in datos1:
        familia=Familiar()
        familia.nombre=familiares[0]
        familia.apellido = familiares[1]
        familia.telefono = familiares[2]
        familia.ciudad = familiares[3]
        familia.parentesco=familiares[4]
        lista_familiar.append(familia)

    conector.close()
def VerBaseDatos():
    """Este metodo sirve para ver la base de datos """
    import sqlite3
    conector = sqlite3.connect("AgendaContactos.db")
    cursor = conector.cursor()
    cursor.execute("select * from FAMILIARES")
    datos = cursor.fetchall()
    for familia in datos:
        print(familia)

def menu():
    cont=1
    while cont!=0:
        print('1-crear amigo')
        print('2-crear familiare')
        print('3-ver amigo')
        print('4-ver familiares')
        print('5-modificar amigo')
        print('6-modificar familiar')
        print('7-ingresar listas en base de datos')
        print('8-cargar listas desde la base de datos')
        print('9-ver base de datos')
        opc=int(input('escribe la opcion'))
        if opc==1:
            InsertarAmigo()
        elif opc==2:
            InsertarFamiliar()
        elif opc==3:
            VerAmigo()
        elif opc==4:
            VerFamiliar()
        elif opc==5:
            ModificarAmigo()
        elif opc==6:
            ModificarFamiliar()
        elif opc==7:
            GuardarBaseDatos()
        elif opc==8:
            CargarBaseDatos()
        elif opc == 9:
            VerBaseDatos()
menu()
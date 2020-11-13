class Empleado:
    def __init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.anosAnt = anosAnt
        self.tel = tel
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        print("DNI: ", self.dni)
        print("Dirección: ", self.direccion)
        print("Años de Antiguedad: ", self.anosAnt)
        print("Teléfono: ", self.tel)
        print("Salario: ", self.salario)
        print("Supervisor: ", self.supervisor)

    def cambiarSupervisor(self, supervisor):
        self.supervisor = supervisor
        print("El nuevo supervisor es: ", self.supervisor)

    def incremetarSalario(self, porcen):
        nuevoSalario = 0
        if(porcen == Secretario(Empleado).salario):
            nuevoSalario = (Secretario.salario * porcen) + Secretario(Empleado).salario
            print("El salario del Secretario ahora es de: ", nuevoSalario, "€")
        elif(porcen == Vendedor(Empleado).porcenSal):
            nuevoSalario = (Vendedor(Empleado).salario * porcen) + Vendedor(Empleado).salario
            print("El salario del Vendedor ahora es de: ", nuevoSalario, "€")
        elif(porcen == Jefe.porcensal):
            nuevoSalario = (Jefe(Empleado).salario * porcen) + Jefe(Empleado).salario
            print("El salario del Jefe ahora es de: ", nuevoSalario, "€")
        else:
            print("No es un porcentaje válido")

class Secretario(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor, despacho, nFax, porcenSal):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor)
        self.despacho = despacho
        self.nFax = nFax
        self.porcenSal = porcenSal

    def imprimir(self):
        Empleado.imprimir(self)
        print("El despacho es: ", self.despacho)
        print("El Número de Fax es: ", self.nFax)

class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor, matCoche, marcaCoche, modeloCoche, area, listaClientes, porcen, porcenSal):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor)
        self.matCoche = matCoche
        self.marcaCoche = marcaCoche
        self.modeloCoche = modeloCoche
        self.area = area
        self.listaClientes = listaClientes
        self.porcen = porcen
        self.porcenSal = porcenSal

    def imprimir(self):
        Empleado.imprimir(self)
        print("La matrícula de coche es: ", self.matCoche)
        print("La marca del cohe es: ", self.marcaCoche)
        print("El modelo del coche es: ", self.modeloCoche)
        print("El área de ventas es: ", self.area)
        print("Los clientes son: ")

        for x in self.listaClientes:
            print(x)

        print("El porcentaje de ventas es: ", self.porcen)

    def altaCliente(self, cliente):
        lista = self.listaClientes
        lista.append(cliente)
        print("Ahora los clientes son: ")
        for x in lista:
            print(x)

    def bajaCliente(self, cliente):
        lista = self.listaClientes
        lista.remove(cliente)
        print("Ahora los clientes son: ")
        for x in lista:
            print(x)

    def cambiarCoche(self, mat, marca, modelo):
        self.matCoche = mat
        self.marcaCoche = marca
        self.modeloCoche = modelo
        print("Ahora las características de coche son: ")
        print("Matrícula: ", self.matCoche)
        print("Marca: ", self.marcaCoche)
        print("Modelo: ", self.modeloCoche)

class Jefe(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor, despacho, secretario, listaVendedores, matCoche, marcaCoche, modeloCoche, porcenSal):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, anosAnt, tel, salario, supervisor)
        self.despacho = despacho
        self.secretario = secretario
        self.listaVendedores = listaVendedores
        self.matCoche = matCoche
        self.marcaCoche = marcaCoche
        self.modeloCoche = modeloCoche
        self.porcenSal = porcenSal

    def imprimir(self):
        Empleado.imprimir(self)
        print("El despacho es: ", self.despacho)
        print("El secretario es: ", self.secretario)
        print("Los vendedores son: ")

        for x in self.listaVendedores:
            print(x)

        print("La matrícula de coche es: ", self.matCoche)
        print("La marca del cohe es: ", self.marcaCoche)
        print("El modelo del coche es: ", self.modeloCoche)

    def cambiarSecretario(self, secretario):
        self.secretario = secretario
        print("El nuevo secretario es: ", self.secretario)

    def cambiarCoche(self, mat, marca, modelo):
        Vendedor.cambiarCoche(mat, marca, modelo)

    def altaVendedor(self, vendedor, area):
        lista = self.listaVendedores
        if (area == Vendedor(Empleado).area):
            lista.append(vendedor)
        print("Ahora los clientes son: ")
        for x in lista:
            print(x)

    def bajaVendedor(self, vendedor, area):
        lista = self.listaVendedores
        if (area == Vendedor(Empleado).area):
            lista.remove(vendedor)
        print("Ahora los clientes son: ")
        for x in lista:
            print(x)

sec0 = Secretario

sec1 = Secretario("Maria", "Luna", "11111111K", "Calle Consorcio", 2, 111111111, 2000, sec0, "Despacho 3", 7, 5)
sec2 = Secretario("Pau", "Salazar", "22222222K", "Calle Cuadrilla", 1, 222222222, 1000, sec0, "Despacho 2", 4, 5)
sec3 = Secretario("Rebeca", "Mateo", "88888888K", "Calle Leroi", 9, 333333333, 4000, sec0, "Despacho 1", 2, 5)

listaCli1 = ["cli1", "cli2", "cli3", "cli4"]
listaCli2 = ["cli1", "cli2", "cli3", "cli4"]

ven1 = Vendedor("Pedro", "Romero", "11111111K", "Calle Romero", 5, 111111111, 1500, sec1, "h23i4g", "Citroen", "1k", "Informática", listaCli1, 30, 10)
ven2 = Vendedor("Juan", "Martínez", "22222222K", "Calle Perejil", 6, 22222222, 2500, sec2, "g345t5", "Audi", "A6", "Ventas", listaCli2, 50, 10)
ven3 = Vendedor("David", "Gonzalez", "33333333K", "Calle Amaranto", 7, 333333333, 3500, sec1, "745yc7", "BMW", "Sport", "Social", listaCli1, 20, 10)

listaVend1 = [ven1, ven2, ven3]
listaVend2 = [ven1, ven2, ven3]
listaVend3 = [ven1, ven2, ven3]

je1 = Jefe("Alvaro", "Romero", "11111111K", "Calle Romero", 10, 34553454, 5500, "Sin supervisor", "Despacho 2", sec1, listaVend1, "h768ww", "Audi", "2Da", 20)
je2 = Jefe("Paco", "Ramirez", "22222222K", "Calle Haya", 13, 74846736, 6500, "Sin supervisor", "Despacho 4", sec2, listaVend2, "76f96f", "BMW", "8i0", 20)
je3 = Jefe("Andres", "Yecla", "33333333K", "Calle Yota", 20, 54324234, 8500, "Sin supervisor", "Despacho 6", sec1, listaVend3, "74gh84", "Mercedes", "7k7", 20)

ven1.incremetarSalario(ven1, 20)


class Alumno:
    def __init__(self, rut, nombre, apellido, fecha_nacimiento, carrera):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera
        self.asignaturas = []

    def agregar_asignatura(self, nombre_asignatura, promedio):
        asignatura = {'nombre': nombre_asignatura, 'promedio': promedio}
        self.asignaturas.append(asignatura)

    def obtener_promedio_total(self):
        total = 0
        for asignatura in self.asignaturas:
            total += asignatura['promedio']
        return total / len(self.asignaturas)


def grabar_alumno():
    rut = input("Ingrese el Rut del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    
    alumno = Alumno(rut, nombre, apellido, fecha_nacimiento, carrera)
    
    agregar_asignaturas = True
    while agregar_asignaturas:
        nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
        promedio = float(input("Ingrese el promedio de la asignatura: "))
        alumno.agregar_asignatura(nombre_asignatura, promedio)
        
        respuesta = input("¿Desea agregar más asignaturas? (S/N): ")
        if respuesta.upper() != "S":
            agregar_asignaturas = False
            
    # Guardar el alumno en una lista o base de datos
    # Por simplicidad, en este ejemplo lo guardaremos en una lista
    alumnos.append(alumno)
    
    print("Alumno registrado correctamente.\n")


def buscar_alumno():
    rut_buscar = input("Ingrese el Rut del alumno a buscar: ")
    
    for alumno in alumnos:
        if alumno.rut == rut_buscar:
            print("Información del alumno:")
            print("Rut:", alumno.rut)
            print("Nombre:", alumno.nombre)
            print("Apellido:", alumno.apellido)
            print("Fecha de Nacimiento:", alumno.fecha_nacimiento)
            print("Carrera:", alumno.carrera)
            
            if alumno.asignaturas:
                print("Asignaturas:")
                for asignatura in alumno.asignaturas:
                    print("- Nombre:", asignatura['nombre'])
                    print("- Promedio:", asignatura['promedio'])
                    
            print()
            return
    
    print("No se encontró ningún alumno con ese Rut.\n")


def imprimir_certificados():
    rut_certificado = input("Ingrese el Rut del alumno para imprimir el certificado: ")
    
    for alumno in alumnos:
        if alumno.rut == rut_certificado:
            print("Tipos de certificados:")
            print("1. Certificado de Alumno Regular de Notas")
            print("2. Certificado de Matrícula")
            opcion_certificado = input("Seleccione el tipo de certificado a imprimir (1/2): ")
            
            if opcion_certificado == "1":
                print("Certificado de Alumno Regular de Notas")
                print("Nombre:", alumno.nombre)
                print("Rut:", alumno.rut)
                print("Carrera:", alumno.carrera)
                
                if alumno.asignaturas:
                    print("Asignaturas y Promedios:")
                    for asignatura in alumno.asignaturas:
                        print("- Asignatura:", asignatura['nombre'])
                        print("- Promedio:", asignatura['promedio'])
                        
            elif opcion_certificado == "2":
                certificado = str(randint(1000, 5000))
                print("Certificado de Matrícula")
                print("Nombre:", alumno.nombre)
                print("Rut:", alumno.rut)
                print("Carrera:", alumno.carrera)
                print("Número de Certificado:", certificado)
                
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.\n")
                return
            
            print()
            return
    
    print("No se encontró ningún alumno con ese Rut.\n")


# Lista para almacenar los alumnos registrados
alumnos = []

# Función principal
def main():
    while True:
        print("Menú:")
        print("1. Grabar")
        print("2. Buscar")
        print("3. Imprimir certificados")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            grabar_alumno()
        elif opcion == "2":
            buscar_alumno()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.\n")


# Iniciar el programa
if __name__ == "__main__":
    main()
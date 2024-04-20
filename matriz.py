class Nodo:
    def __init__(self, placa=None, color=None, linea=None, modelo=None, propietario=None):
        self.placa = placa
        self.color = color
        self.linea = linea
        self.modelo = modelo
        self.propietario = propietario
        self.abajo = None
        self.derecha = None

class MatrizOrtogonal:
    def __init__(self):
        self.cabecera_filas = Nodo()  # Inicio de Filas
        self.cabecera_columnas = Nodo()  # Inicio de columnas
        self.construir_matriz()

    def construir_matriz(self):
        # Creacion de filas y conexion
        fila_actual = self.cabecera_filas
        for _ in range(10):
            fila_actual.abajo = Nodo()
            fila_actual = fila_actual.abajo

        # Creacion de columnas y conexion
        columna_actual = self.cabecera_columnas
        for _ in range(10):
            columna_actual.derecha = Nodo()
            columna_actual = columna_actual.derecha

    def insertar(self, placa, color, linea, modelo, propietario, fila, columna):
        nuevo_nodo = Nodo(placa, color, linea, modelo, propietario)
        
        # Insertar  fila
        nodo_fila = self.cabecera_filas
        for _ in range(fila):
            nodo_fila = nodo_fila.abajo
        nuevo_nodo.abajo = nodo_fila.abajo
        nodo_fila.abajo = nuevo_nodo
        
        # Insertar  columna
        nodo_columna = self.cabecera_columnas
        for _ in range(columna):
            nodo_columna = nodo_columna.derecha
        nuevo_nodo.derecha = nodo_columna.derecha
        nodo_columna.derecha = nuevo_nodo

    def buscar(self, criterios):
        resultados = []
        nodo_fila_actual = self.cabecera_filas.abajo
        while nodo_fila_actual:
            nodo_actual = nodo_fila_actual.derecha
            while nodo_actual:
                coincide = all(getattr(nodo_actual, prop) == valor for prop, valor in criterios.items())
                if coincide:
                    resultados.append(nodo_actual)
                nodo_actual = nodo_actual.derecha
            nodo_fila_actual = nodo_fila_actual.abajo
        return resultados

    def eliminar(self, criterios):
        nodos_a_eliminar = self.buscar(criterios)
        for nodo in nodos_a_eliminar:
            # Encontrar el nodo anterior en la fila
            nodo_anterior_fila = self.cabecera_filas
            while nodo_anterior_fila.abajo != nodo:
                nodo_anterior_fila = nodo_anterior_fila.abajo

            # Encontrar el nodo anterior en la columna
            nodo_anterior_columna = self.cabecera_columnas
            while nodo_anterior_columna.derecha != nodo:
                nodo_anterior_columna = nodo_anterior_columna.derecha

            # Eliminar referencias al nodo en la fila
            nodo_anterior_fila.abajo = nodo.abajo

            # Eliminar referencias al nodo en la columna
            nodo_anterior_columna.derecha = nodo.derecha

# Funcion para imprimir la matriz
def imprimir_matriz(matriz):
    nodo_fila = matriz.cabecera_filas.abajo
    while nodo_fila:
        nodo_actual = nodo_fila.derecha
        while nodo_actual:
            if nodo_actual.placa is not None:
                print("*", end=" ")
            else:
                print("-", end=" ")
            nodo_actual = nodo_actual.derecha
        print()
        nodo_fila = nodo_fila.abajo

# Funcion principal del programa
def main():
    matriz = MatrizOrtogonal()

    # Espacios ocupados iniciales (primeros 24 espacios)
    datos_iniciales = [
        ("ABC123", "Rojo", "Sedan", 2020, "Juan", 0, 0),
        ("XYZ789", "Azul", "SUV", 2019, "Maria", 1, 1),
        ("DEF456", "Verde", "Compacto", 2021, "Pedro", 2, 2),
    ]
    for placa, color, linea, modelo, propietario, fila, columna in datos_iniciales:
        matriz.insertar(placa, color, linea, modelo, propietario, fila, columna)

    while True:
        print("\nOpciones:")
        print("1. Insertar vehiculo")
        print("2. Buscar vehículo")
        print("3. Eliminar vehículo")
        print("4. Imprimir matriz")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            placa = input("Ingrese la placa del vehiculo: ")
            color = input("Ingrese el color del vehiculo: ")
            linea = input("Ingrese la linea del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            propietario = input("Ingrese el propietario del vehiculo: ")
            fila = int(input("Ingrese la fila donde desea insertar el vehiculo (0-9): "))
            columna = int(input("Ingrese la columna donde desea insertar el vehiculo (0-9): "))
            matriz.insertar(placa, color, linea, modelo, propietario, fila, columna)
            print("Vehiculo insertado exitosamente.")
        elif opcion == "2":
            criterios = {}
            criterios["placa"] = input("Ingrese la placa del vehiculo a buscar: ")
            resultados = matriz.buscar(criterios)
            if resultados:
                print("Vehiculo(s) encontrado(s):")
                for vehiculo in resultados:
                    print(f"Placa: {vehiculo.placa}, Color: {vehiculo.color}, Linea: {vehiculo.linea}, Modelo: {vehiculo.modelo}, Propietario: {vehiculo.propietario}")
            else:
                print("No se encontraron vehiculos con los criterios proporcionados.")
        elif opcion == "3":
            criterios = {}
            criterios["placa"] = input("Ingrese la placa del vehiculo a eliminar: ")
            matriz.eliminar(criterios)
            print("Vehiculo eliminado exitosamente.")
        elif opcion == "4":
            imprimir_matriz(matriz)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.")

if __name__ == "__main__":
    main()
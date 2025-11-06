import os

menu = """
      SELECCIONE EL NUMERO DE LA OPCION QUE DESEA LEER:
        1. Tema, problema y solucion
        2. Dataset de referencia 
        3. Estructura por tabla (tipo y escala) 
        4. Escalas de medición 
        5. Sugerencias y mejoras con Copilot 
        6. Salir
      """
      
opt1 = """
        TEMA:
        Aurelion es un supermercado mayorista dedicado a la distribución de productos de consumo diario, como bebidas, alimentos envasados, etc.
        El objetivo es modernizar la gestión comercial y administrativa del mayorista mediante la digitalización de los procesos de ventas, control de stock y 
        análisis de rentabilidad, reemplazando la administración manual por un sistema automatizado que integre toda la información clave del negocio y facilite la toma de decisiones.

        PROBLEMA:
        El dueño del kiosko tiene dificultades para registrar correctamente los movimientos de caja del negocio y controlar el stock porque 
        gestiona las ventas y los productos de forma manual y en distintos archivos, lo que provoca errores y desactualización de datos. 
        El dinero en caja no coincide con el stock disponible debido a olvidos en el registro de ventas o cálculos imprecisos en los pagos. 
        Estos errores ocurren porque no existe un sistema automatizado que integre la información ni genere alertas sobre movimientos o inconsistencias. 
        Además, la falta de una base de datos centralizada impide identificar los productos más vendidos y las categorías más rentables. 
        En consecuencia, la ausencia de un sistema de gestión integral provoca desorden administrativo y pérdidas económicas.

        SOLUCIÓN PROPUESTA:
        Implementar una plataforma digital integral para el supermercado mayorista, basada en Python, que automatice la gestión de ventas, control de stock y análisis financiero. 
        El sistema permitirá la carga y actualización de datos desde archivos Excel y CSV, generará reportes interactivos y alertas automáticas sobre inconsistencias de stock 
        y movimientos de caja, y ofrecerá herramientas para identificar tendencias de productos y categorías más rentables. 
        Además, facilitará la exportación de información para su análisis en Power BI asegurando una administración eficiente, segura y escalable.
    """


opt2 = """
        DATASET DE REFERENCIA

        FUENTE:
        - productos.xlsx: Lista de productos con su categoría y precio unitario.
        - clientes.xlsx: Registro de clientes con su información de contacto.
        - ventas.xlsx: Detalle de cada venta realizada, incluyendo fecha, cliente y medio de pago.
        - detalle_ventas.xlsx: Detalle de productos incluidos en cada venta, con cantidad y precio.

        DEFINICION (campos principales):

        productos.xlsx (~100 filas)
        - id_producto      | int | Escala: Nominal | Identificador único del producto
        - nombre_producto  | str | Escala: Nominal | Nombre del producto
        - categoria        | str | Escala: Nominal | Categoría a la que pertenece
        - precio_unitario  | int | Escala: Razón   | Precio por unidad del producto

        clientes.xlsx (~100 filas)
        - id_cliente       | int | Escala: Nominal | Identificador único del cliente
        - nombre_cliente   | str | Escala: Nominal | Nombre del cliente
        - email            | str | Escala: Nominal | Correo electrónico del cliente
        - ciudad           | str | Escala: Nominal | Ciudad del cliente
        - fecha_alta       | str | Escala: Nominal | Fecha de alta del cliente

        ventas.xlsx (~120 filas)
        - id_venta         | int | Escala: Nominal | Identificador único de la venta
        - fecha            | str | Escala: Nominal | Fecha en que se realizó la venta
        - id_cliente       | int | Escala: Nominal | Identificador del cliente
        - nombre_cliente   | str | Escala: Nominal | Nombre del cliente
        - email            | str | Escala: Nominal | Correo electrónico del cliente
        - medio_pago       | str | Escala: Nominal | Medio de pago utilizado

        detalle_ventas.xlsx (~120 filas)
        - id_venta         | int | Escala: Nominal | Identificador único del detalle
        - id_producto      | int | Escala: Nominal | Identificador del producto
        - nombre_producto  | str | Escala: Nominal | Nombre del producto
        - cantidad         | int | Escala: Razón   | Cantidad vendida del producto
        - precio_unitario  | int | Escala: Razón   | Precio por unidad del producto
        - importe          | int | Escala: Razón   | Importe total (cantidad * precio)
    """

opt3 = """
        ESTRUCTURA POR TABLA (TIPO Y ESCALA)

        productos.xlsx
        - id_producto     (int, Nominal)
        - nombre_producto (str, Nominal)
        - categoria       (str, Nominal)
        - precio_unitario (int, Razón)

        clientes.xlsx
        - id_cliente      (int, Nominal)
        - nombre_cliente  (str, Nominal)
        - email           (str, Nominal)
        - ciudad          (str, Nominal)
        - fecha_alta      (str, Nominal)

        ventas.xlsx
        - id_venta        (int, Nominal)
        - fecha           (str, Nominal)
        - id_cliente      (int, Nominal)
        - nombre_cliente  (str, Nominal)
        - email           (str, Nominal)
        - medio_pago      (str, Nominal)

        detalle_ventas.xlsx
        - id_venta        (int, Nominal)
        - id_producto     (int, Nominal)
        - nombre_producto (str, Nominal)
        - cantidad        (int, Razón)
        - precio_unitario (int, Razón)
        - importe         (int, Razón)
    """

opt4 = """
        ESCALAS DE MEDICION

        - Nominal: Clasifica datos en categorías sin orden intrínseco. Solo permite igualdad/diferencia.
          Ejemplos en el dataset: categoria (bebidas, snacks), ciudad, medio_pago, nombre_producto, email.

        - Razón: Datos numéricos con cero absoluto y proporciones significativas.
          Permite operaciones aritméticas completas (sumar, promediar, multiplicar).
          Ejemplos en el dataset: precio_unitario, cantidad, importe.
    """

opt5 = """
        SUGERENCIAS Y MEJORAS CON COPILOT

        - Implementar validaciones de entrada para evitar errores por datos incorrectos.
        - Permitir la carga y actualización de datos desde archivos CSV además de Excel.
        - Agregar exportación de reportes en diferentes formatos (PDF, Excel).
        - Incorporar autenticación básica para proteger el acceso al sistema.
        - Mejorar la interfaz de usuario en consola con colores y formato.
        - Automatizar la generación de gráficos simples desde Python.
        - Documentar el código fuente con comentarios y ejemplos de uso.
        - Modularizar el programa en funciones y clases para facilitar el mantenimiento.
        - Añadir logs de actividad para auditoría y seguimiento de errores.
        - Permitir la integración con otros sistemas mediante API REST en el futuro.
    """


def leer_opcion():
    while True:
        opt = input("Ingrese opción: ")
        try:
            opcion = int(opt)
        except ValueError:
            print("\nEntrada inválida. Ingrese un número del 1 al 6.\n")
            continue
        if 1 <= opcion <= 6:
            return opcion
        print("\nOPCION INCORRECTA, INGRESE UNA OPCION VALIDA (1-6).\n")


def pausa():
    input("\n\nPresione Enter para continuar...")


while True:
    os.system('cls')
    print(menu)
    opcion = leer_opcion()

    if opcion == 6:
        os.system('cls')
        print("\n\n\nSaliendo...\n\n\n")
        break

    match opcion:
        case 1:
            os.system('cls')
            print(opt1)
            pausa()
        case 2:
            os.system('cls')
            print(opt2)
            pausa()
        case 3:
            os.system('cls')
            print(opt3)
            pausa()
        case 4:
            os.system('cls')
            print(opt4)
            pausa()
        case 5:
            os.system('cls')
            print(opt5)
            pausa()

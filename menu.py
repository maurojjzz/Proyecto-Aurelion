import os

menu = """
            SELECCIONE EL NUMERO DE LA OPCION QUE DESEA LEER / EJECUTAR:
                1. Tema, problema y solucion
                2. Dataset de referencia 
                3. Estructura por tabla (tipo y escala) 
                4. Escalas de medición 
                5. Sugerencias y mejoras con Copilot 
                6. Análisis completo (rankings + medios de pago)
                7. Ver gráficos específicos
                8. Regenerar datos limpios (limpieza)
                9. Salir
            """
      
opt1 = """
        TEMA:
        Aurelion es un supermercado mayorista dedicado a la distribución de productos de consumo diario, como bebidas, alimentos envasados, etc. El objetivo es modernizar la gestión comercial y administrativa del mayorista mediante la digitalización de los procesos de ventas, control de stock y análisis de rentabilidad, reemplazando la administración manual por un sistema automatizado que integre toda la información clave del negocio y facilite la toma de decisiones.

        PROBLEMA:
        El supermercado no cuenta con una forma clara de analizar qué productos se venden más, cómo pagan los clientes y qué artículos tienen poca rotación. La información está dispersa en distintos archivos y no se puede obtener fácilmente un análisis de ventas, métodos de pago o desempeño de productos.

        SOLUCIÓN PROPUESTA:
        Implementar un sistema que unifique los datos de ventas, clientes y productos para generar automáticamente:
        - un dataset combinado con toda la información (ventas, clientes, productos) para análisis centralizado.
        - ranking de productos y categorías según unidades vendidas e importe total (acumulado).
        - análisis de medios de pago (ventas, importe total, ticket promedio, clientes únicos) y segmentación de clientes por frecuencia de compra.

        El sistema permitirá identificar qué productos rinden, cómo prefieren pagar los clientes y cuáles casi no se venden, mejorando decisiones de surtido, promociones y control de stock.
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
        
        dataset_completo.csv (~120 filas)
        - id_venta         | int  | Escala: Nominal | ID de la venta (join principal)
        - id_producto      | int  | Escala: Nominal | ID del producto
        - cantidad         | int  | Escala: Razón   | Unidades del producto en esa venta
        - importe          | int  | Escala: Razón   | Importe de la línea (cantidad * precio_unitario)
        - fecha            | str  | Escala: Nominal | Fecha de la venta (AAAA-MM-DD)
        - id_cliente       | int  | Escala: Nominal | ID del cliente
        - medio_pago       | str  | Escala: Nominal | Medio de pago utilizado
        - ciudad           | str  | Escala: Nominal | Ciudad del cliente
        - fecha_alta       | str  | Escala: Nominal | Fecha de alta del cliente
        - categoria        | str  | Escala: Nominal | Categoría del producto
        - precio_unitario  | int  | Escala: Razón   | Precio unitario del producto (normalizado)
        - nombre_producto  | str  | Escala: Nominal | Nombre del producto (normalizado)
        - nombre_cliente   | str  | Escala: Nominal | Nombre del cliente (normalizado)
        - email            | str  | Escala: Nominal | Email del cliente
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
        
        dataset_completo.csv
        - id_venta        (int, Nominal)
        - id_producto     (int, Nominal)
        - cantidad       (int, Razón)
        - importe        (int, Razón)
        - fecha          (str, Nominal)
        - id_cliente     (int, Nominal)
        - medio_pago     (str, Nominal)
        - ciudad         (str, Nominal)
        - fecha_alta     (str, Nominal)
        - categoria      (str, Nominal)
        - precio_unitario(int, Razón)
        - nombre_producto(str, Nominal)
        - nombre_cliente (str, Nominal)
        - email          (str, Nominal)
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
        if 1 <= opcion <= 9:
            return opcion
        print("\nOPCION INCORRECTA, INGRESE UNA OPCION VALIDA (1-9).\n")


def pausa():
    input("\n\nPresione Enter para continuar...")


while True:
    os.system('cls')
    print(menu)
    opcion = leer_opcion()

    if opcion == 9:
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
        case 6:
            # Ejecutar análisis completo
            os.system('cls')
            print("Ejecutando análisis completo...\n")
            try:
                import analisis
                analisis.run_full_analysis()
            except Exception as e:
                print(f"Error al ejecutar análisis: {e}")
            pausa()
        case 7:
            # Sub-menú de gráficos específicos
            os.system('cls')
            print("Sub-menú de gráficos:\n")
            print("  1. Top productos por unidades")
            print("  2. Top productos por importe")
            print("  3. Top categorías por unidades")
            print("  4. Top categorías por importe")
            print("  5. Resumen medios de pago (barras)")
            print("  6. Heatmaps medios de pago vs segmento")
            print("  7. Volver")
            sub = input("Seleccione opción de gráfico: ")
            try:
                sub = int(sub)
            except ValueError:
                print("Opción inválida.")
                pausa(); continue
            if sub == 7:
                continue
            try:
                import analisis
                df_tmp = analisis.load_data()
                rankings = analisis.compute_rankings(df_tmp)
                pay = analisis.payment_analysis(df_tmp)
                if sub == 1:
                    analisis.plot_top_products_units(rankings)
                elif sub == 2:
                    analisis.plot_top_products_importe(rankings)
                elif sub == 3:
                    analisis.plot_top_categories_units(rankings)
                elif sub == 4:
                    analisis.plot_top_categories_importe(rankings)
                elif sub == 5:
                    analisis.plot_payment_summary(pay)
                elif sub == 6:
                    analisis.plot_payment_heatmaps(pay)
                else:
                    print("Opción de gráfico inválida.")
            except Exception as e:
                print(f"Error generando gráfico: {e}")
            pausa()
        case 8:
            # Regenerar datos limpios
            os.system('cls')
            print("Regenerando datos limpios (limpieza.py)...\n")
            try:
                import limpieza
                print("Limpieza ejecutada. Archivos interim actualizados.")
            except Exception as e:
                print(f"Error al ejecutar limpieza: {e}")
            pausa()

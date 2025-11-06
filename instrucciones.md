# Instrucciones para GitHub Copilot

## Proyecto: Sistema de Gestión Aurelion
*Supermercado mayorista - Gestión de ventas, stock y análisis financiero*

---

## 🎯 Objetivo Principal
Desarrollar una plataforma digital integral basada en Python que automatice la gestión comercial y administrativa del supermercado mayorista Aurelion, reemplazando los procesos manuales por un sistema integrado y eficiente.

---

## 📋 Mejoras y Funcionalidades a Implementar

### 1. 🔐 Validación y Seguridad
- **Validaciones de entrada**: Implementar controles para evitar errores por datos incorrectos
- **Autenticación básica**: Proteger el acceso al sistema con login/password
- **Logs de actividad**: Sistema de auditoría y seguimiento de errores

### 2. 📊 Gestión de Datos
- **Carga de archivos**: Permitir importación desde Excel (.xlsx) y CSV
- **Actualización de datos**: Sistema para modificar información existente
- **Base de datos centralizada**: Integrar toda la información del negocio

### 3. 📈 Reportes y Análisis
- **Exportación múltiple**: Generar reportes en PDF, Excel y otros formatos
- **Gráficos automatizados**: Crear visualizaciones simples desde Python
- **Análisis de rentabilidad**: Identificar productos y categorías más rentables
- **Integración Power BI**: Exportar datos para análisis avanzado

### 4. 🚨 Alertas y Control
- **Alertas automáticas**: Notificaciones sobre inconsistencias de stock
- **Control de caja**: Verificación de movimientos y coincidencias
- **Gestión de inventario**: Seguimiento en tiempo real del stock

### 5. 💻 Interfaz y Experiencia
- **Mejora visual**: Colores y formato mejorado en consola
- **Menú interactivo**: Navegación intuitiva y clara
- **Mensajes de error**: Feedback claro para el usuario

### 6. 🔧 Arquitectura y Mantenimiento
- **Modularización**: Organizar código en funciones y clases
- **Documentación**: Comentarios y ejemplos de uso
- **Escalabilidad**: Preparar para futuras integraciones
- **API REST**: Posibilidad de integración con otros sistemas

---

## 📁 Estructura de Archivos del Dataset

### productos.xlsx (~100 filas)
```
- id_producto      | int | Identificador único
- nombre_producto  | str | Nombre del producto
- categoria        | str | Categoría (bebidas, snacks, etc.)
- precio_unitario  | int | Precio por unidad
```

### clientes.xlsx (~100 filas)
```
- id_cliente       | int | Identificador único
- nombre_cliente   | str | Nombre completo
- email            | str | Correo electrónico
- ciudad           | str | Ubicación
- fecha_alta       | str | Fecha de registro
```

### ventas.xlsx (~120 filas)
```
- id_venta         | int | Identificador único
- fecha            | str | Fecha de venta
- id_cliente       | int | Cliente asociado
- nombre_cliente   | str | Nombre del cliente
- email            | str | Email del cliente
- medio_pago       | str | Método de pago
```

### detalle_ventas.xlsx (~120 filas)
```
- id_venta         | int | Identificador de venta
- id_producto      | int | Producto vendido
- nombre_producto  | str | Nombre del producto
- cantidad         | int | Unidades vendidas
- precio_unitario  | int | Precio por unidad
- importe          | int | Total (cantidad × precio)
```

---

## 🚀 Prioridades de Implementación

### Sprint 1 (Actual) ✅
- [x] Menú interactivo básico
- [x] Documentación del sistema
- [x] Estructura de datos definida

### Sprint 2 (Siguiente)
- [ ] Carga de archivos Excel/CSV
- [ ] Validaciones de entrada
- [ ] Reportes básicos

### Sprint 3 (Futuro)
- [ ] Análisis de rentabilidad
- [ ] Sistema de alertas
- [ ] Mejoras de interfaz

---

## 💡 Consejos para el Desarrollo

1. **Mantener simplicidad**: Comenzar con funcionalidades básicas y expandir gradualmente
2. **Reutilizar código**: Crear funciones modulares y reutilizables
3. **Manejar errores**: Implementar try/catch para operaciones críticas
4. **Documentar cambios**: Comentar el código y mantener documentación actualizada
5. **Testear funcionalidades**: Probar cada nueva característica antes de integrar

---

## 📞 Contexto del Problema
El supermercado mayorista Aurelion necesita modernizar su gestión manual que causa:
- Errores en registro de ventas
- Descontrol de stock
- Pérdidas económicas por inconsistencias
- Falta de análisis de rentabilidad
- Desorganización administrativa

**La solución debe ser integral, automatizada y escalable.**
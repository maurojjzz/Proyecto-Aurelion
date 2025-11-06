"""
Limpieza y diagnóstico básico de datasets.
"""

import os
import pandas as pd
import unicodedata

RAW_DIR = "./data/raw"
INTERIM_DIR = "./data/interim"
os.makedirs(INTERIM_DIR, exist_ok=True)

clientes_df = pd.read_excel(f"{RAW_DIR}/clientes.xlsx")
ventas_df = pd.read_excel(f"{RAW_DIR}/ventas.xlsx")
productos_df = pd.read_excel(f"{RAW_DIR}/productos.xlsx")
detalle_ventas_df = pd.read_excel(f"{RAW_DIR}/detalle_ventas.xlsx")

print("\n\n===== CLIENTES =====")
print("Shape:", clientes_df.shape)
clientes_df.info()
print("\nDescribe:\n", clientes_df.describe())
print("\nPrimeras filas:\n", clientes_df.head())
print("\nNulos por columna:\n", clientes_df.isnull().sum())
print("\nDuplicados por fila completa:", clientes_df.duplicated().sum())
clientes_df = clientes_df.drop_duplicates()

print("\n\n===== VENTAS =====")
print("Shape:", ventas_df.shape)
ventas_df.info()
print("\nDescribe:\n", ventas_df.describe())
print("\nPrimeras filas:\n", ventas_df.head())
print("\nNulos por columna:\n", ventas_df.isnull().sum())
print("\nDuplicados por fila completa:", ventas_df.duplicated().sum())
ventas_df = ventas_df.drop_duplicates()

print("\n\n===== PRODUCTOS =====")
print("Shape:", productos_df.shape)
productos_df.info()
print("\nDescribe:\n", productos_df.describe())

nombre_col = "nombre_producto"
categoria_col = "categoria"

if nombre_col not in productos_df.columns or categoria_col not in productos_df.columns:
	print("Las columnas esperadas no están en 'productos': se esperaban 'nombre_producto' y 'categoria'.")
else:
	kw_alimentos = [
		"coca", "pepsi", "sprite", "fanta", "agua", "gaseosa", "jugo", "energetica", "energética",
		"yerba", "te", "té", "cafe", "café", "leche", "yogur", "yogurt", "queso", "manteca",
		"pan", "medialuna", "medialunas", "bizcocho", "bizcochos", "galletita", "galletitas", "alfajor",
		"papas fritas", "papas", "mani", "maní", "frutos secos", "chocolate", "turron", "turrón",
		"barrita", "cereal", "caramelo", "caramelos", "chicle", "chupetin", "chupetín",
		"dulce de leche", "mermelada", "miel", "stevia", "granola", "avena",
		"pizza", "empanadas", "verduras congeladas", "hamburguesas",
		"aceite", "vinagre", "salsa", "tomate", "arroz", "fideos", "lentejas", "garbanzos", "porotos",
		"harina", "azucar", "azúcar", "sal", "aceitunas", "aceituna",
		"jugo en polvo", "sopa instantanea", "sopa instantánea", "caldo",
		"cerveza", "vino", "sidra", "fernet", "vodka", "ron", "gin", "whisky", "licor", "helado"
	]

	def _norm_text(s: str) -> str:
		s = str(s).lower()
		return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

	name_norm = productos_df[nombre_col].astype(str).apply(_norm_text)
	kw_alimentos_norm = [_norm_text(k) for k in kw_alimentos]

	# Máscara de alimento: True si el nombre contiene alguna palabra clave de alimentos (contiene, no igualdad)
	mask_alimento = False
	for kw in kw_alimentos_norm:
		mask_alimento = (name_norm.str.contains(kw, na=False)) | mask_alimento

	# Asignación simple: por defecto 'Limpieza', si matchea -> 'Alimento'
	productos_df[categoria_col] = "Limpieza"
	productos_df.loc[mask_alimento, categoria_col] = "Alimento"

print("\nPrimeras filas:\n", productos_df.head())
print("\nNulos por columna:\n", productos_df.isnull().sum())
print("\nDuplicados por fila completa:", productos_df.duplicated().sum())
productos_df = productos_df.drop_duplicates()



# --- DETALLE VENTAS ---
print("\n\n===== DETALLE VENTAS =====")
print("Shape:", detalle_ventas_df.shape)
detalle_ventas_df.info()
print("\nDescribe:\n", detalle_ventas_df.describe()) 
print("\nPrimeras filas:\n", detalle_ventas_df.head())
print("\nNulos por columna:\n", detalle_ventas_df.isnull().sum())
print("\nDuplicados por fila completa:", detalle_ventas_df.duplicated().sum())
detalle_ventas_df = detalle_ventas_df.drop_duplicates()

clientes_df.to_csv(f"{INTERIM_DIR}/clientes.csv", index=False)
ventas_df.to_csv(f"{INTERIM_DIR}/ventas.csv", index=False)
productos_df.to_csv(f"{INTERIM_DIR}/productos.csv", index=False)
detalle_ventas_df.to_csv(f"{INTERIM_DIR}/detalle_ventas.csv", index=False)






import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo
sns.set(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (8, 5)
pd.set_option("display.max_columns", None)

# Aca voy a traer los archivos limpios
clientes = pd.read_csv('./data/interim/clientes.csv')
ventas = pd.read_csv('./data/interim/ventas.csv')
productos = pd.read_csv('./data/interim/productos.csv')
detalle_ventas = pd.read_csv('./data/interim/detalle_ventas.csv')

print("Clientes:", clientes.shape)
print("Productos:", productos.shape)
print("Ventas:", ventas.shape)
print("Detalle Ventas:", detalle_ventas.shape)
print("\n==========================================\n")

# Aca voy a joinear los datasets para tener toda la info en uno dataframe
df = (
    detalle_ventas
    .merge(ventas, on='id_venta', how='left')
    .merge(clientes, on='id_cliente', how='left')
    .merge(productos, on='id_producto', how='left')
    )

if 'precio_unitario_x' in df.columns:
    df['precio_unitario'] = df['precio_unitario_x']
    df.drop(['precio_unitario_x', 'precio_unitario_y'], axis=1, inplace=True)

if 'nombre_producto_x' in df.columns:
    df['nombre_producto'] = df['nombre_producto_y']  
    df.drop(['nombre_producto_x', 'nombre_producto_y'], axis=1, inplace=True)

if 'nombre_cliente_x' in df.columns:
    df['nombre_cliente'] = df['nombre_cliente_y']  
    df.drop(['nombre_cliente_x', 'nombre_cliente_y'], axis=1, inplace=True)

if 'email_x' in df.columns:
    df['email'] = df['email_y']  
    df.drop(['email_x', 'email_y'], axis=1, inplace=True)

print("Dataframe combinado:", df.shape)

print(df.info())

# voy a crear la nueva tabla combinada
df.to_csv('./data/interim/dataset_completo.csv', index=False, encoding='utf-8')


# Visualizacion y calculos
# Rankings de productos y categorías por unidades (cantidad) e importe (facturación)

top_n = 10

# Asegurar tipos numéricos
df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(0).astype(int)
df['importe'] = pd.to_numeric(df['importe'], errors='coerce').fillna(0)

# Productos: ranking por unidades
ranking_prod_unidades = (
        df.groupby(['id_producto', 'nombre_producto'], as_index=False)['cantidad']
            .sum()
            .rename(columns={'cantidad': 'unidades_vendidas'})
            .sort_values('unidades_vendidas', ascending=False)
)

# Productos: ranking por importe (incluye unidades totales del producto)
ranking_prod_importe = (
        df.groupby(['id_producto', 'nombre_producto'], as_index=False)
            .agg(unidades_vendidas=('cantidad', 'sum'), importe_total=('importe', 'sum'), precio_unitario=('precio_unitario', 'mean'))
            .sort_values('importe_total', ascending=False)
)
ranking_prod_importe['precio_unitario'] = ranking_prod_importe['precio_unitario'].round(0).astype(int)

# Categorías: ranking por unidades
ranking_cat_unidades = (
        df.groupby(['categoria'], as_index=False)['cantidad']
            .sum()
            .rename(columns={'cantidad': 'unidades_vendidas'})
            .sort_values('unidades_vendidas', ascending=False)
)

# Categorías: ranking por importe
ranking_cat_importe = (
        df.groupby(['categoria'], as_index=False)['importe']
            .sum()
            .rename(columns={'importe': 'importe_total'})
            .sort_values('importe_total', ascending=False)
)

print("\n=== Top 10 productos por unidades vendidas ===")
print(ranking_prod_unidades.head(top_n).to_string(index=False))

print("\n=== Top 10 productos por importe (facturación) ===")
print(
    ranking_prod_importe.head(top_n)[['id_producto','nombre_producto','unidades_vendidas','precio_unitario','importe_total']]
    .to_string(index=False)
)

print("\n=== Top 10 categorías por unidades vendidas ===")
print(ranking_cat_unidades.head(top_n).to_string(index=False))

print("\n=== Top 10 categorías por importe (facturación) ===")
print(ranking_cat_importe.head(top_n).to_string(index=False))

# Exportar resultados a CSV
ranking_prod_unidades.to_csv('./data/interim/ranking_productos_unidades.csv', index=False, encoding='utf-8')
ranking_prod_importe.to_csv('./data/interim/ranking_productos_importe.csv', index=False, encoding='utf-8')
ranking_cat_unidades.to_csv('./data/interim/ranking_categorias_unidades.csv', index=False, encoding='utf-8')
ranking_cat_importe.to_csv('./data/interim/ranking_categorias_importe.csv', index=False, encoding='utf-8')

# Gráficos simples (Top 10) guardados como PNG
try:
        top_prod_unidades = ranking_prod_unidades.head(top_n)
        top_prod_importe = ranking_prod_importe.head(top_n)
        top_cat_unidades = ranking_cat_unidades.head(top_n)
        top_cat_importe = ranking_cat_importe.head(top_n)

        plt.figure()
        sns.barplot(data=top_prod_unidades, x='unidades_vendidas', y='nombre_producto', orient='h')
        plt.title('Top 10 Productos por Unidades Vendidas')
        plt.tight_layout()
        plt.savefig('./data/interim/top10_productos_unidades.png')
        plt.close()

        plt.figure()
        sns.barplot(data=top_prod_importe, x='importe_total', y='nombre_producto', orient='h')
        plt.title('Top 10 Productos por Importe (Facturación)')
        plt.tight_layout()
        plt.savefig('./data/interim/top10_productos_importe.png')
        plt.close()

        plt.figure()
        sns.barplot(data=top_cat_unidades, x='unidades_vendidas', y='categoria', orient='h')
        plt.title('Top 10 Categorías por Unidades Vendidas')
        plt.tight_layout()
        plt.savefig('./data/interim/top10_categorias_unidades.png')
        plt.close()

        plt.figure()
        sns.barplot(data=top_cat_importe, x='importe_total', y='categoria', orient='h')
        plt.title('Top 10 Categorías por Importe (Facturación)')
        plt.tight_layout()
        plt.savefig('./data/interim/top10_categorias_importe.png')
        plt.close()
except Exception as e:
        print(f"Aviso: no se pudieron generar gráficos. Detalle: {e}")


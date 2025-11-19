import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (8, 5)
pd.set_option("display.max_columns", None)

def load_data():
    clientes = pd.read_csv('./data/interim/clientes.csv')
    ventas = pd.read_csv('./data/interim/ventas.csv')
    productos = pd.read_csv('./data/interim/productos.csv')
    detalle_ventas = pd.read_csv('./data/interim/detalle_ventas.csv')
    print("Clientes:", clientes.shape)
    print("Productos:", productos.shape)
    print("Ventas:", ventas.shape)
    print("Detalle Ventas:", detalle_ventas.shape)
    df = (
        detalle_ventas
        .merge(ventas, on='id_venta', how='left')
        .merge(clientes, on='id_cliente', how='left')
        .merge(productos, on='id_producto', how='left')
    )
    for col_base in ['precio_unitario', 'nombre_producto', 'nombre_cliente', 'email']:
        x = f'{col_base}_x'; y = f'{col_base}_y'
        if x in df.columns:
            df[col_base] = df[y] if col_base != 'precio_unitario' else df[x]
            drop_cols = [c for c in [x, y] if c in df.columns]
            df.drop(drop_cols, axis=1, inplace=True)
    print("Dataframe combinado:", df.shape)
    df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(0).astype(int)
    df['importe'] = pd.to_numeric(df['importe'], errors='coerce').fillna(0)
    return df

def compute_rankings(df, top_n=10):
    ranking_prod_unidades = (df.groupby(['id_producto','nombre_producto'], as_index=False)['cantidad']
        .sum().rename(columns={'cantidad':'unidades_vendidas'})
        .sort_values('unidades_vendidas', ascending=False))
    ranking_prod_importe = (df.groupby(['id_producto','nombre_producto'], as_index=False)
        .agg(unidades_vendidas=('cantidad','sum'), importe_total=('importe','sum'), precio_unitario=('precio_unitario','mean'))
        .sort_values('importe_total', ascending=False))
    ranking_prod_importe['precio_unitario'] = ranking_prod_importe['precio_unitario'].round(0).astype(int)
    ranking_cat_unidades = (df.groupby(['categoria'], as_index=False)['cantidad']
        .sum().rename(columns={'cantidad':'unidades_vendidas'})
        .sort_values('unidades_vendidas', ascending=False))
    ranking_cat_importe = (df.groupby(['categoria'], as_index=False)['importe']
        .sum().rename(columns={'importe':'importe_total'})
        .sort_values('importe_total', ascending=False))
    return {
        'ranking_prod_unidades': ranking_prod_unidades,
        'ranking_prod_importe': ranking_prod_importe,
        'ranking_cat_unidades': ranking_cat_unidades,
        'ranking_cat_importe': ranking_cat_importe,
        'top_n': top_n
    }

def print_rankings(r):
    top_n = r['top_n']
    print("\n=== Top 10 productos por unidades vendidas ===")
    print(r['ranking_prod_unidades'].head(top_n).to_string(index=False))
    print("\n=== Top 10 productos por importe (facturación) ===")
    print(r['ranking_prod_importe'].head(top_n)[['id_producto','nombre_producto','unidades_vendidas','precio_unitario','importe_total']].to_string(index=False))
    print("\n=== Top 10 categorías por unidades vendidas ===")
    print(r['ranking_cat_unidades'].head(top_n).to_string(index=False))
    print("\n=== Top 10 categorías por importe (facturación) ===")
    print(r['ranking_cat_importe'].head(top_n).to_string(index=False))

def plot_top_products_units(r):
    top = r['ranking_prod_unidades'].head(r['top_n'])
    plt.figure(); sns.barplot(data=top, x='unidades_vendidas', y='nombre_producto', orient='h'); plt.title('Top Productos por Unidades'); plt.tight_layout(); plt.show(); plt.close()

def plot_top_products_importe(r):
    top = r['ranking_prod_importe'].head(r['top_n'])
    plt.figure(); sns.barplot(data=top, x='importe_total', y='nombre_producto', orient='h'); plt.title('Top Productos por Importe'); plt.tight_layout(); plt.show(); plt.close()

def plot_top_categories_units(r):
    top = r['ranking_cat_unidades'].head(r['top_n'])
    plt.figure(); sns.barplot(data=top, x='unidades_vendidas', y='categoria', orient='h'); plt.title('Top Categorías por Unidades'); plt.tight_layout(); plt.show(); plt.close()

def plot_top_categories_importe(r):
    top = r['ranking_cat_importe'].head(r['top_n'])
    plt.figure(); sns.barplot(data=top, x='importe_total', y='categoria', orient='h'); plt.title('Top Categorías por Importe'); plt.tight_layout(); plt.show(); plt.close()

def payment_analysis(df):
    resumen_pago = (df.groupby('medio_pago').agg(ventas=('id_venta','nunique'), importe_total=('importe','sum'), clientes_unicos=('id_cliente','nunique'))
        .assign(ticket_promedio=lambda x: (x['importe_total']/x['ventas']).round(2))
        .sort_values('importe_total', ascending=False))
    ventas_por_cliente = df.groupby('id_cliente')['id_venta'].nunique()
    q25, q75 = ventas_por_cliente.quantile([0.25,0.75])
    def clasificar_segmento(n):
        if n <= q25: return 'Baja'
        if n >= q75: return 'Alta'
        return 'Media'
    segmento_cliente = ventas_por_cliente.apply(clasificar_segmento)
    segmento_cliente.name = 'segmento'
    df_segmentado = df.merge(segmento_cliente, on='id_cliente', how='left')
    cruce = (df_segmentado.groupby(['medio_pago','segmento']).agg(ventas=('id_venta','nunique'), importe_total=('importe','sum')).reset_index())
    tabla_imp = cruce.pivot(index='medio_pago', columns='segmento', values='importe_total').fillna(0)
    tabla_ven = cruce.pivot(index='medio_pago', columns='segmento', values='ventas').fillna(0)
    return {
        'resumen_pago': resumen_pago,
        'cruce': cruce,
        'tabla_imp': tabla_imp,
        'tabla_ven': tabla_ven,
        'q25': q25,
        'q75': q75
    }

def print_payment_tables(p):
    print("\nResumen por medio de pago:"); print(p['resumen_pago'].to_string())
    print("\nMedio de pago vs segmento:"); print(p['cruce'].to_string(index=False))
    print("\nImporte total por medio_pago y segmento:"); print(p['tabla_imp'].to_string())
    print("\nVentas por medio_pago y segmento:"); print(p['tabla_ven'].to_string())
    mp_top = p['resumen_pago'].index[0]
    print("\n=== Insights Métodos de Pago ===")
    print(f"Medio de pago con mayor facturación: {mp_top}")
    print(f"Q25={p['q25']}, Q75={p['q75']} (segmentación frecuencia)")

def plot_payment_summary(p):
    plt.figure(); p['resumen_pago'].reset_index().plot(kind='bar', x='medio_pago', y='importe_total', legend=False, color='steelblue'); plt.title('Importe Total por Medio de Pago'); plt.ylabel('Importe Total'); plt.tight_layout(); plt.show(); plt.close()
    plt.figure(); p['resumen_pago'].reset_index().plot(kind='bar', x='medio_pago', y='ventas', legend=False, color='darkorange'); plt.title('Cantidad de Ventas por Medio de Pago'); plt.ylabel('Ventas'); plt.tight_layout(); plt.show(); plt.close()

def plot_payment_heatmaps(p):
    plt.figure(); sns.heatmap(p['tabla_imp'], annot=True, fmt='.0f', cmap='Blues'); plt.title('Importe Total (Medio Pago vs Segmento)'); plt.tight_layout(); plt.show(); plt.close()
    plt.figure(); sns.heatmap(p['tabla_ven'], annot=True, fmt='.0f', cmap='Oranges'); plt.title('Ventas (Medio Pago vs Segmento)'); plt.tight_layout(); plt.show(); plt.close()

def run_full_analysis():
    df = load_data()
    df.to_csv('./data/interim/dataset_completo.csv', index=False, encoding='utf-8')
    rankings = compute_rankings(df)
    print_rankings(rankings)
    pay = payment_analysis(df)
    print_payment_tables(pay)
    # Mostrar gráficos principales
    plot_top_products_units(rankings)
    plot_top_products_importe(rankings)
    plot_top_categories_units(rankings)
    plot_top_categories_importe(rankings)
    plot_payment_summary(pay)
    plot_payment_heatmaps(pay)

if __name__ == '__main__':
    run_full_analysis()

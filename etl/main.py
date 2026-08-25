# ETM Mmodule laden
import etl.extract as et
import etl.transform as tr
import etl.load as lo

# sku_raw = etl.extract.extract_sku()
# sku = tr.transform_sku(sku_raw)

# Verbindung zu Datenbank herstellen und alle Zeilen löschen
engine = lo.get_engine()
lo.truncate_all(engine)

dim_sku = lo.load_dimension(tr.transform_sku(et.extract_sku()), 'dim_sku', engine)
dim_mitarbeiter = lo.load_dimension(tr.transform_mitarbeiter(et.extract_mitarbeiter()), 'dim_mitarbeiter', engine)
dim_typ = lo.load_dimension(tr.transform_typ(et.extract_typ()), 'dim_typ', engine)
dim_tische = lo.load_dimension(tr.transform_tische(et.extract_tische()), 'dim_tisch', engine)
dim_orte = lo.load_dimension(tr.transform_orte(et.extract_orte()), 'dim_ort', engine)

sales = tr.transform_sales(et.extract_sales())
sales = lo.resolve_key(sales, 'tisch_key', dim_tische, 'tisch', 'tisch_key')
sales = lo.resolve_key(sales, 'mitarbeiter_key', dim_mitarbeiter, 'mitarbeiter_id', 'mitarbeiter_key')
sales = lo.resolve_key(sales, 'typ_key', dim_typ, 'typ', 'typ_key')
sales = lo.resolve_key(sales, 'sku', dim_sku, 'sku', 'sku_key')
sales = lo.resolve_key(sales, 'standort', dim_orte, 'id', 'ort_key')
sales = sales.rename(columns={'sku': 'sku_key', 'standort': 'ort_key'})

lo.load_fact(sales, 'fact_sales', engine)

# Daten in Warehouse laden
from sqlalchemy import create_engine, text
import pandas as pd
from etl.config import DB_CONNECTION_STRING

def get_engine():
    return create_engine(DB_CONNECTION_STRING)

def truncate_all(engine):
    """Leert alle Dimensions- und Faktentabellen und setzt die Surrogate Keys
    zurück, damit main.py gefahrlos neu ausgeführt werden kann."""
    tables = ['fact_sales', 'dim_sku', 'dim_mitarbeiter', 'dim_typ', 'dim_tisch', 'dim_ort']
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {', '.join(tables)} RESTART IDENTITY CASCADE"))

def load_dimension(df, table_name, engine):
    """Schreibt df in die Zieltabelle (Surrogate Key wird von Postgres vergeben)
    und liest die Tabelle danach zurück, inkl. generierter Keys."""
    df.to_sql(table_name, engine, if_exists='append', index=False)
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

def resolve_key(df, column, dim_df, natural_key, surrogate_key):
    """Ersetzt eine natürliche Schlüsselspalte in df durch den zugehörigen
    Surrogate Key aus einer bereits geladenen dim_df (z.B. tisch_key statt Konto Name)."""
    df = df.copy()
    mapping = dim_df.set_index(dim_df[natural_key].astype(str))[surrogate_key]
    df[column] = df[column].astype(str).map(mapping)
    return df

def load_fact(df, table_name, engine):
    """Schreibt die Faktentabelle in die Zieltabelle. Anders als bei den
    Dimensionen gibt es keinen von Postgres generierten Key zum Zurücklesen."""
    df.to_sql(table_name, engine, if_exists='append', index=False)
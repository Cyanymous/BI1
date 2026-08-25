# Daten aus Flat Files extrahieren
import pandas as pd
from etl.config import RAW_DATA_DIR

# ------------------------------------------------------------
# Dimensionstabellen laden
# ------------------------------------------------------------

def extract_sku():
    return pd.read_csv(RAW_DATA_DIR / 'menu.csv')

def extract_mitarbeiter():
    return pd.read_csv(RAW_DATA_DIR / 'staff.csv')

def extract_typ():
    return pd.read_csv(RAW_DATA_DIR / 'typ.csv')

def extract_tische():
    return pd.read_csv(RAW_DATA_DIR / 'tische.csv')

def extract_orte():
    return pd.read_csv(RAW_DATA_DIR / 'locations.csv')


# ------------------------------------------------------------
# Faktentabllen laden
# ------------------------------------------------------------
def extract_sales():
    alle_dfs = [pd.read_csv(f) for f in (RAW_DATA_DIR / 'generated').glob("pos_*.csv")]
    gesamt = pd.concat(alle_dfs, ignore_index=True)
    return gesamt

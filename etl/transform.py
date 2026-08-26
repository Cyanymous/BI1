import pandas as pd
# Tabellenspalten müssen für alle Tabellen mit den in schema.sql definierten Spalten übereinstimmen!

# ---------------Dimensionstabellen---------------
def transform_sku(df):
    df = df.copy()
    df.columns = ['sku', 'produktname', 'produktgruppe', 'produktbeschreibung', 'produktpreis', 'produktsteuer']
    return df

def transform_mitarbeiter(df):
    df = df.copy()
    df.columns = ['mitarbeiter_id', 'mitarbeiter_name', 'mitarbeiter_gruppe']
    return df

def transform_typ(df):
    df = df.copy()
    df.columns = ['typ', 'beschreibung']
    return df

def transform_tische(df):
    df = df.copy()
    df.columns = ['tisch', 'bereich']
    return df

def transform_orte(df):
    df = df.copy()
    df.columns = ['id', 'plz', 'stadt', 'lat', 'lon', 'liegenschaft']
    return df

# ---------------Faktentabellen---------------
# viele Spalten der Faktentabelle sind für unsere Auswertungen irrelevant und werden gelöscht
def transform_sales(df):
    df = df.copy()
    df = df.drop(columns = [
        'Perioden Id', 'Jahres Id', 'Geräte_Name', 'Modus', 'Konto', 'Referenz',
        'Einzelpreis', 'Rabatt', 'Materialverlust/Bruch', 'Gratis', 'Buchung', 'Artikel',
        'Gruppe', 'StatGruppe', 'SteuerName', 'SteuerRate', 'Profil'
    ])
    df.columns = [
        'identifikator','standort', 'zeitpunkt', 'tisch_key', 'mitarbeiter_key', 'typ_key',
        'menge', 'finalpreis', 'sku', 'vorsteuern', 'steuernmenge'
        ]
    df['zeitpunkt'] = pd.to_datetime(df['zeitpunkt'], format='%d.%m.%y %H:%M')
    df['tisch_key'] = df['tisch_key'].str.extract(r'(\d+)').astype('Int64')
    return df

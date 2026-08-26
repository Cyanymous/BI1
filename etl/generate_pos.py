# POS Daten anhand echter Praxisdaten generieren
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed für Reproduzierbarkeit
np.random.seed(2)

# Fixe Variablen
# Tageszeiten und deren gewichtete Nachfragen
HOURS = list(range(8, 21))
HOUR_WEIGHTS = np.asarray([2, 2, 4, 8, 9, 6, 2, 4, 6, 8, 8, 9, 6])
HOUR_WEIGHTS = HOUR_WEIGHTS / HOUR_WEIGHTS.sum()

DAYS = 14
MEAN_ORDERS_PER_DAY = 80
MAX_ITEMS_PER_ORDER = 4
MAX_NUMBER_PER_ITEM = 3
START_DATE = datetime(2026, 6, 1)

# Bestehende POS Daten laden, um Schlüssel über Aussehen von echten POS Daten zu ziehen
pos_import = pd.read_csv('data/raw/pos_berlin.csv')
columns = pos_import.columns.insert(4, 'Standort')

# Orte laden
locations = (
    pd.read_csv('data/raw/locations.csv')
    .pipe(lambda d: (d['Stadt'] + '-' + d['PLZ'].astype(str)).tolist())
)

 
# Frei erfundene Speisekarte: (SKU, Artikel, Gruppe, Einzelpreis, SteuerRate, Popularität)
menu = [
    ('100', 'Fischbrötchen Backfisch', 'Hauptspeisen', 6.50, 1.07, 6),
    ('101', 'Lachs', 'Hauptspeisen', 14.50, 1.07, 3),
    ('102', 'Matjes', 'Hauptspeisen', 13.50, 1.07, 3),
    ('103', 'Fischbrötchen Räucherlachs', 'Hauptspeisen', 6.90, 1.07, 5),
    ('104', 'Thunfisch Wrap', 'Hauptgerichte', 10.90, 1.07, 5),
    ('105', 'Garnelen-Kimchi-Bruger', 'Hauptgerichte', 11.50, 1.07, 4),
    ('106', 'Neptun-Ringe', 'Beilagen', 7.90, 1.07, 3),
    ('107', 'Chicken Burger', 'Hauptgerichte', 10.90, 1.07, 6),
    ('108', 'Seelachs-Ei-Baugette', 'Hauptgerichte', 9.80, 1.07, 4),
    ('109', 'Bismarck-Baguette', 'Hauptgerichte', 10.90, 1.07, 4),
    ('110', 'Matjes-Baguette', 'Hauptgerichte', 11.90, 1.07, 4),
    ('111', 'Pommes Frites', 'Beilagen', 5.50, 1.07, 8),
    ('112', 'Kartoffelwedges', 'Beilagen', 4.90, 1.07, 5),
    ('113', 'Garnelen Box', 'Beilagen', 6.90, 1.07, 3),
    ('114', 'Fisch Nuggets Box', 'Beilagen', 5.50, 1.07, 3),
    ('115', 'Tiramisu', 'Desserts', 7.90, 1.07, 2),
    ('116', 'Vanillequark', 'Desserts', 5.90, 1.07, 2),
    ('117', 'Rote Grütze', 'Desserts', 5.90, 1.07, 2),
    ('118', 'Schokokuchen', 'Desserts', 6.50, 1.07, 2),
    ('119', 'Cola', 'Getränke', 3.90, 1.19, 7),
    ('120', 'Apfelschorle', 'Getränke', 3.20, 1.19, 5),
    ('121', 'Mineralwasser', 'Getränke', 2.80, 1.19, 6),
    ('122', 'Bier', 'Getränke', 4.20, 1.19, 6),
    ('123', 'Inger-Limonade', 'Getränke', 5.90, 1.19, 2),
    ('124', 'Cola Zero', 'Getränke', 3.90, 1.19, 4),
    ('125', 'Zitronen-Limonade', 'Getränke', 5.90, 1.19, 3),
    ('126', 'Spezi', 'Getränke', 3.90, 1.19, 5),
    ('127', 'Alkoholfreies Bier', 'Getränke', 3.90, 1.19, 3),
]
# Gewichte extrahieren
menu_base_weights = pd.DataFrame(menu)[5].to_numpy() 



# Für jeden Ort aus Locations eine csv mit generierte Sales Daten erzeugen
# Iterieren über die locations und gleichzeitig einen index erzeugen
for loc_idx, loc in enumerate(locations, start=1):

    # Fixe Variablen festelge, die für jede Buchung gleich sind oder den gleichen Aufbau haben
    store_id = 1000000 + loc_idx
    period = np.random.randint(1, 52)
    device = f"iPad1({store_id})"
    employees = np.random.choice(range(101,121), size = 7)

    row_counter = np.random.randint(10000, 90000)
    konto_counter = np.random.randint(6000, 6999)

    # Jeder Standort bekommt sein seinen "eigenen Geschmack"
    # Weight müssen am Ende in Summe 1 ergeben, damit Verteilung funktioniert
    per_location_menu_weights = menu_base_weights * np.random.uniform(0.6, 1.4, size=len(menu))
    per_location_menu_weights /= per_location_menu_weights.sum() 

    rows = []
    # Duch jeden Tag iterieren und Sales generieren
    # Anzahl 
    for day in range(DAYS):
        current_date = START_DATE + timedelta(days=day)
        orders_today = int(np.random.normal(loc = MEAN_ORDERS_PER_DAY, scale=MEAN_ORDERS_PER_DAY*0.2))

        # Durch jede Order des Tages iterieren
        # Hinweis: _ ist Loop Variable, welche nie genutzt wird
        for _ in range(orders_today):
            konto_counter += 1
            order_hour = np.random.choice(a=HOURS, p = HOUR_WEIGHTS)
            order_time = current_date + timedelta(
                hours=int(order_hour), minutes=int(np.random.randint(0, 59))
            )
            mitarbeiter = np.random.choice(employees)
            konto_name = f"Tisch {np.random.randint(1, 25)}" if np.random.random() > 0.1 else ''
            n_items = np.random.randint(1, MAX_ITEMS_PER_ORDER)
            typ = np.random.choice(['SALE', 'VOID'], p=[0.9, 0.1])

            for _ in range(n_items):
                sku, artikel, gruppe, einzelpreis, steuer_rate, _ = menu[np.random.choice(len(menu), p=per_location_menu_weights)]
                menge = np.random.randint(1, MAX_NUMBER_PER_ITEM)
                final_preis = round(einzelpreis * menge, 2)
                vor_steuern = round(final_preis / steuer_rate, 6)
                steuern_menge = round(final_preis - vor_steuern, 6)
                steuer_name = f"MwSt. {round((steuer_rate - 1) * 100)}%"

                row_counter += 1
                identifikator = f"S{store_id}.{row_counter}"

                rows.append({
                    'Identifikator': identifikator,
                    'Perioden Id': f"SP{store_id}.{period}.{row_counter}",
                    'Jahres Id': f"SY{store_id}.{order_time.year}.{row_counter}",
                    'Geräte_Name': device,
                    'Standort': loc_idx,
                    'Datum': order_time.strftime('%d.%m.%y %H:%M'),
                    'Modus': 'Prod',
                    'Konto': f"A{store_id}.{konto_counter}",
                    'Konto Name': konto_name,
                    'Mitarbeiter': mitarbeiter,
                    'Referenz': identifikator,
                    'Typ': typ,
                    'Mng': menge,
                    'Einzelpreis': einzelpreis,
                    'FinalPreis': final_preis,
                    'Rabatt': 0.0,
                    'Materialverlust/Bruch': 0.0,
                    'Gratis': 0.0,
                    'Buchung': 0.0,
                    'SKU': sku,
                    'Artikel': artikel,
                    'Gruppe': gruppe,
                    'StatGruppe': '',
                    'SteuerName': steuer_name,
                    'SteuerRate': steuer_rate,
                    'VorSteuern': vor_steuern,
                    'SteuernMenge': steuern_menge,
                    'Profil': 'Normalverkauf',
                })

    pos_loc = pd.DataFrame(rows, columns=columns)
    pos_loc.to_csv(f'data/raw/generated/pos_{loc.lower()}.csv', index=False)

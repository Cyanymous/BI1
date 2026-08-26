# Modul zur Erzeugung der Dimensionsdaten
import pandas as pd
import random as random
import numpy as np

# ------------------------------------------------------------
# Proudukte
# ------------------------------------------------------------
menu = [
    ('100', 'Fischbrötchen Backfisch', 'Hauptspeisen', 'Knuspriger Backfisch im Brötchen mit Remoulade', 6.50, 1.07),
    ('101', 'Lachs', 'Hauptspeisen', 'Gebratenes Lachsfilet mit hausgemachter Sauce', 14.50, 1.07),
    ('102', 'Matjes', 'Hauptspeisen', 'Matjesfilet nach Hausfrauenart mit Zwiebeln und Apfel', 13.50, 1.07),
    ('103', 'Fischbrötchen Räucherlachs', 'Hauptspeisen', 'Brötchen mit hauchdünn geschnittenem Räucherlachs', 6.90, 1.07),
    ('104', 'Thunfisch Wrap', 'Hauptgerichte', 'Wrap mit gegrilltem Thunfisch und frischem Salat', 10.90, 1.07),
    ('105', 'Garnelen-Kimchi-Bruger', 'Hauptgerichte', 'Burger mit Garnelen und würzigem Kimchi', 11.50, 1.07),
    ('106', 'Neptun-Ringe', 'Beilagen', 'Frittierte Fischringe mit Dip nach Wahl', 7.90, 1.07),
    ('107', 'Chicken Burger', 'Hauptgerichte', 'Knuspriger Hähnchen-Burger mit frischem Salat', 10.90, 1.07),
    ('108', 'Seelachs-Ei-Baugette', 'Hauptgerichte', 'Baguette mit gebratenem Seelachs und Ei', 9.80, 1.07),
    ('109', 'Bismarck-Baguette', 'Hauptgerichte', 'Baguette mit Bismarckhering und roten Zwiebeln', 10.90, 1.07),
    ('110', 'Matjes-Baguette', 'Hauptgerichte', 'Baguette mit Matjesfilet und Gurke', 11.90, 1.07),
    ('111', 'Pommes Frites', 'Beilagen', 'Klassische Pommes frites, knusprig frittiert', 5.50, 1.07),
    ('112', 'Kartoffelwedges', 'Beilagen', 'Würzige Kartoffelecken mit Schale', 4.90, 1.07),
    ('113', 'Garnelen Box', 'Beilagen', 'Knackige Garnelen mit Dip zum Teilen', 6.90, 1.07),
    ('114', 'Fisch Nuggets Box', 'Beilagen', 'Panierte Fischnuggets mit Sauce', 5.50, 1.07),
    ('115', 'Tiramisu', 'Desserts', 'Italienisches Tiramisu mit Espresso und Mascarpone', 7.90, 1.07),
    ('116', 'Vanillequark', 'Desserts', 'Cremiger Vanillequark, leicht gesüßt', 5.90, 1.07),
    ('117', 'Rote Grütze', 'Desserts', 'Fruchtige Rote Grütze mit Vanillesauce', 5.90, 1.07),
    ('118', 'Schokokuchen', 'Desserts', 'Saftiger Schokokuchen mit Schokoladenüberzug', 6.50, 1.07),
    ('119', 'Cola', 'Getränke', 'Cola, 0,3l, gekühlt', 3.90, 1.19),
    ('120', 'Apfelschorle', 'Getränke', 'Apfelschorle, 0,3l, spritzig', 3.20, 1.19),
    ('121', 'Mineralwasser', 'Getränke', 'Stilles oder spritziges Mineralwasser, 0,3l', 2.80, 1.19),
    ('122', 'Bier', 'Getränke', 'Fassbier, frisch gezapft, 0,3l', 4.20, 1.19),
    ('123', 'Inger-Limonade', 'Getränke', 'Hausgemachte Ingwer-Limonade, spritzig-scharf', 5.90, 1.19),
    ('124', 'Cola Zero', 'Getränke', 'Cola ohne Zucker, 0,3l, gekühlt', 3.90, 1.19),
    ('125', 'Zitronen-Limonade', 'Getränke', 'Erfrischende Zitronen-Limonade, 0,3l', 5.90, 1.19),
    ('126', 'Spezi', 'Getränke', 'Spezi (Cola-Orangenlimo-Mix), 0,3l', 3.90, 1.19),
    ('127', 'Alkoholfreies Bier', 'Getränke', 'Alkoholfreies Bier, 0,3l', 3.90, 1.19),
]
menu_df = pd.DataFrame(menu, columns=['SKU', 'Produktname', 'Produktgruppe','Produktbeschreibung', 'Einzelpreis', 'Steuer'])
menu_df.to_csv('data/raw/menu.csv', index = False)


# ------------------------------------------------------------
# Mitarbeiter
# ------------------------------------------------------------
mitarbeiter = [
    ('101', 'Ana Bergmann', 'Manager'),
    ('102', 'Max Hoffmann', 'Aushilfe'),
    ('103', 'Lea Schneider', 'Vollzeit'),
    ('104', 'Tom Richter', 'Aushilfe'),
    ('105', 'Nina Wolf', 'Vollzeit'),
    ('106', 'Jan Krüger', 'Manager'),
    ('107', 'Mia Zimmermann', 'Aushilfe'),
    ('108', 'Paul Neumann', 'Vollzeit'),
    ('109', 'Emma Schwarz', 'Aushilfe'),
    ('110', 'Leon Braun', 'Vollzeit'),
    ('111', 'Sophie Vogel', 'Manager'),
    ('112', 'Finn Krause', 'Aushilfe'),
    ('113', 'Hannah Lehmann', 'Vollzeit'),
    ('114', 'Luca Fischer', 'Aushilfe'),
    ('115', 'Marie Köhler', 'Vollzeit'),
    ('116', 'Ben Peters', 'Aushilfe'),
    ('117', 'Laura Huber', 'Vollzeit'),
    ('118', 'Elias Meyer', 'Manager'),
    ('119', 'Julia Franke', 'Aushilfe'),
    ('120', 'David Sommer', 'Vollzeit'),
]
mitarbeiter_df = pd.DataFrame(mitarbeiter, columns = ['ID', 'Name', 'Gruppe'])
mitarbeiter_df.to_csv('data/raw/staff.csv', index = False)

# ------------------------------------------------------------
# Tische
# ------------------------------------------------------------
tische = pd.DataFrame({
    'Tisch': range (1,26),
    'Bereich': ['Innenbereich'] * 15 + ['Außenbereich'] * 10
})
tische.to_csv('data/raw/tische.csv', index = False)

# ------------------------------------------------------------
# Orte
# ------------------------------------------------------------
stadt = pd.read_csv('data/raw/Liste-Staedte-in-Deutschland.csv', sep=';')
locations = stadt.sample(n=400, replace=False, random_state=1)

# Austauschen von '/' mit '-' damit keine Probleme in Dateinamen entstehen und ID und Liegenschaft hinzufügen
locations = (
    locations
    .assign(
        Stadt=lambda d: d['Stadt'].str.replace('/', '-', regex=False),
        ID=lambda d: range(1, len(d) + 1),
        Liegenschaft=lambda d: np.random.choice(
            ['Einkaufszentrum', 'Innenstadt', 'Raststätte', 'Andere'],
            size=len(d)
        )
    )
    .drop(columns=['Schlüsselnummer'])
)
locations.to_csv('data/raw/locations.csv', index = False)


# ------------------------------------------------------------
# Typ
# ------------------------------------------------------------
typ = [
    ('SALE', 'Verkauf'),
    ('VOID', 'Storno')
]
typ_df = pd.DataFrame(typ, columns = ['Typ', 'Beschreibung'])
typ_df.to_csv('data/raw/typ.csv', index = False)


# ------------------------------------------------------------
# Location New
# ------------------------------------------------------------
loc_new = pd.read_csv('data/raw/zipcodes.csv', sep=',').sample(n=400, random_state=1)
loc_new = loc_new.assign(
    ID=lambda df: range(1,401),
    ZIPCODE=lambda df: df['ZIPCODE'].str.replace("'", ""),
    NAME=lambda df: df['NAME'].str.replace("'", ""),
    LAT=lambda df: df['LAT'].astype(float),
    LON=lambda df: df['LON'].astype(float),
    liegenschaft=lambda d: np.random.choice(['Einkaufszentrum', 'Innenstadt', 'Raststätte', 'Andere'], size = len(d)) 
)
loc_new = loc_new.drop(columns = ['INDEX'])
loc_new.columns = ['id', 'plz', 'stadt', 'lat', 'lon', 'liegenschaft']
loc_new.to_csv('data/raw/locations.csv', index = False)

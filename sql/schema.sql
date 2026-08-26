-- Datenbank anlegen

-- Dimensionstabellen
CREATE TABLE dim_sku (
    sku_key SERIAL PRIMARY KEY,
    sku VARCHAR(10) UNIQUE NOT NULL,
    produktname VARCHAR(100),
    produktgruppe VARCHAR(50),
    produktbeschreibung VARCHAR(200),
    produktpreis NUMERIC(10,2),
    produktsteuer NUMERIC(4,2)
);

CREATE TABLE dim_mitarbeiter (
    mitarbeiter_key SERIAL PRIMARY KEY,
    mitarbeiter_id VARCHAR(10) UNIQUE NOT NULL,
    mitarbeiter_name VARCHAR(100),
    mitarbeiter_gruppe VARCHAR(30)
);

CREATE TABLE dim_typ (
    typ_key SERIAL PRIMARY KEY,
    typ VARCHAR(10) UNIQUE NOT NULL,
    beschreibung VARCHAR(50)
);

CREATE TABLE dim_tisch (
    tisch_key SERIAL PRIMARY KEY,
    tisch INT UNIQUE NOT NULL,
    bereich VARCHAR(30)
);

CREATE TABLE dim_ort (
    ort_key SERIAL PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    liegenschaft VARCHAR(50),
    stadt VARCHAR(500),
    plz VARCHAR(5),
    lat NUMERIC(9,6),
    lon NUMERIC(9,6)
);

-- Faktentabelle

CREATE TABLE fact_sales (
    identifikator VARCHAR(50),
    zeitpunkt TIMESTAMP,
    tisch_key INT REFERENCES dim_tisch(tisch_key),
    mitarbeiter_key INT REFERENCES dim_mitarbeiter(mitarbeiter_key),
    typ_key INT REFERENCES dim_typ(typ_key),
    sku_key INT REFERENCES dim_sku(sku_key),
    ort_key INT REFERENCES dim_ort(ort_key),
    menge INT,
    finalpreis NUMERIC(10,2),
    vorsteuern NUMERIC(10,2),
    steuernmenge NUMERIC(10,2)
);
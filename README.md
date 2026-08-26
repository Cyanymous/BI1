# Business Intelligence 1

Dies ist ein  Fallstudie im Rahmen des Moduls Business Intelligence (1). Ziel ist es, eine Business Intelligence Lösung für die fiktive Sylter Fischspezialitäten GmbH aufzubauen.

Als fiktives Szenario dienen Kassendaten (Point of Sale) mehrerer Filialen in verschiedenen deutschen Städten. Die Daten werden künstlich generiert.

## Architektur

```
Rohdaten (CSV)  --->  ETL (Python/Pandas)  --->  PostgreSQL (Sternschema)  --->  Metabase (Dashboards)
```

- **Rohdaten**: CSV-Dateien in `data/raw/`, u. a. generierte Kassenbons pro Standort (`data/raw/generated/`)
- **ETL**: Python-Skripte in `etl/`, die Rohdaten extrahieren, transformieren und in die Datenbank laden
- **Data Warehouse**: PostgreSQL-Datenbank mit einem klassischen Sternschema (siehe `sql/schema.sql`)
- **Dashboards**: Metabase zur Visualisierung und Analyse der Daten


```

## Hinweis

Dieses Projekt dient ausschließlich Lernzwecken im Rahmen eines Universitätskurses.

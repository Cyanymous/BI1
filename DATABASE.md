# Database Setup & Reload

Commands for creating, truncating, reloading, and verifying the `dwh` Postgres database.
Run all commands from the project root.

## 1. Start the containers

```bash
docker compose up -d
```

## 2. Create / recreate the schema

Use this when `sql/schema.sql` has changed (e.g. a column type was edited).
This drops **all** tables and data.

```bash
docker exec bi1-postgres-1 psql -U postgres -d dwh -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
docker exec -i bi1-postgres-1 psql -U postgres -d dwh < sql/schema.sql
```

## 3. Load the data

`main.py` truncates all tables itself before loading, so this alone is enough
whenever only the source CSVs changed (schema unchanged). Just rerun it:

```bash
source .venv/bin/activate
python3 -c "import etl.main"
```

## 4. Verify

Row counts:

```bash
docker exec bi1-postgres-1 psql -U postgres -d dwh -c "
SELECT 'dim_sku' t, count(*) FROM dim_sku
UNION ALL SELECT 'dim_mitarbeiter', count(*) FROM dim_mitarbeiter
UNION ALL SELECT 'dim_typ', count(*) FROM dim_typ
UNION ALL SELECT 'dim_tisch', count(*) FROM dim_tisch
UNION ALL SELECT 'dim_ort', count(*) FROM dim_ort
UNION ALL SELECT 'fact_sales', count(*) FROM fact_sales;
"
```

NULL foreign keys in `fact_sales` (a non-zero count means some rows didn't
match a dimension row — check the source data for that column):

```bash
docker exec bi1-postgres-1 psql -U postgres -d dwh -c "
SELECT
  count(*) FILTER (WHERE tisch_key IS NULL) AS null_tisch,
  count(*) FILTER (WHERE mitarbeiter_key IS NULL) AS null_mitarbeiter,
  count(*) FILTER (WHERE typ_key IS NULL) AS null_typ,
  count(*) FILTER (WHERE sku_key IS NULL) AS null_sku,
  count(*) FILTER (WHERE ort_key IS NULL) AS null_ort,
  count(*) AS total
FROM fact_sales;
"
```

from pathlib import Path

# ---------------Pfade---------------
PROJECT_ROOT = Path()
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# ---------------Datenbankverbindung---------------
# Müssen zu den Werten in compose.yaml passen
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "dwh"
DB_USER = "postgres"
DB_PASSWORD = "dwh_pw"

# Fertig zusammengesetzte Connection-URL für SQLAlchemy
DB_CONNECTION_STRING = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

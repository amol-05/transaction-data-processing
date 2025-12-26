from sqlalchemy import create_engine

DATABASE_URL = "oracle+oracledb://appuser:apppassword@localhost:1521/XEPDB1"

# We'll going to change it later when we read data from oracle
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    echo=True
)


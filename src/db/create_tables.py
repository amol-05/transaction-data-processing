from src.db.engine import engine
from src.db.base import Base
from src.db.models.customer import Customer

def create_tables():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()
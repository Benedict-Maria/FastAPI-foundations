from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:%28ct3_1_7ia%29%2A@localhost:3306/studentdb"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
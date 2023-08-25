from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://gimhojun@127.0.0.1:5432/todos"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://hojunkim:W6nJqVOcwS1tGuueSInbANsdWUT1cSws@dpg-cje41ienk9qs73dv4tag-a.singapore-postgres.render.com/winedb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


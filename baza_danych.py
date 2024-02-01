import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# POŁĄCZENIE Z SQL - PARAMETRY #
db_params = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    database="postgres",
    username= "postgres",
    password= "Monika",
    host= "localhost",
    port= 5433)

# ŁĄCZENIE Z SQL #
engine = create_engine(db_params)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

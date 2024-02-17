from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
password = 'Amit@2000'
engine = create_engine(f'postgresql://postgres:{password}@localhost/pizza_delivery',echo=True)

Base = declarative_base()

Session = sessionmaker()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
password = 'thrymr_123'
engine = create_engine(f'postgresql://postgres:{password}@localhost/pizza_delivery',echo=True)

Base = declarative_base()

Session = sessionmaker()

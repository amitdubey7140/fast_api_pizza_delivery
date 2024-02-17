from database.database import engine,Base
from models.models import User,Order

Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import get_config


SQLALCHEMY_DATABASE_URL= get_config("SQLACHEMY_DATABASE_URL")


engine= create_engine(SQLALCHEMY_DATABASE_URL)

Session= sessionmaker(bind=engine)


async def get_db():
    db= Session()
    
    try:
        yield db
    except:
        db.close()



# "postgresql+pg8000://postgres:m03kht4r1999@127.0.0.1/reservationdb"
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/postgres'.format(
            os.environ['db_user'],
            os.environ['db_password'],
            os.environ['db_host'],
            '5432')

engine = create_engine(DB_URI)

Session = sessionmaker(bind=engine)

Base = declarative_base()

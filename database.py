from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:password@127.0.0.1:3306/databasename'
engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf8', echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,expire_on_commit=False)
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "oracle+oracledb://myuser:mypassword@localhost:1521/?service_name=XEPDB1"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Một Base duy nhất
Base = declarative_base()

def init_db():
    # Import tất cả models để chúng đăng ký vào Base
    from models import bangthemmoi_dautu
    
    Base.metadata.create_all(bind=engine)

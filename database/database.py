from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models.models_giao_dich import Base

DATABASE_URL = "postgresql://quanlychitieu_user:MfrzOGP5r1rpO1cRQrsQCw58rIb34fka@dpg-d115toumcj7s739smp30-a.singapore-postgres.render.com/quanlychitieu"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db():
    Base.metadata.create_all(bind=engine)
    print("Bảng đã được tạo hoặc đã tồn tại.")

if __name__ == "__main__":
    create_db()

from fastapi import FastAPI
from database.database import engine
from models.bangthemmoi_dautu import ThemMoiDauTu
from models.base import Base
from app.routers import router_bangthemmoi_dautu as ThemMoiDauTu
from database.database import init_db




app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Chào mừng đến với API của TANTV"}

init_db()

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)



# Đăng ký router
app.include_router(ThemMoiDauTu.router)

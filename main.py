from fastapi import FastAPI
from database.database import engine
from models.base import Base
from app.routers import router_giao_dich as giao_dich
from app.routers import router_thu_nhap as thu_nhap
from app.routers import router_tiet_kiem as tiet_kiem
from app.routers import router_tong_hop as tong_hop
from app.routers import router_danh_muc as danh_muc
from app.routers import router_dau_tu as dau_tu
from app.routers import router_tien_no as tien_no
from app.routers import router_tra_no as tra_no
from database.database import init_db




app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Chào mừng đến với API Quản lý tài chính cá nhân"}

init_db()

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)



# Đăng ký router
app.include_router(giao_dich.router)
app.include_router(thu_nhap.router)
app.include_router(tiet_kiem.router)
app.include_router(tong_hop.router)
app.include_router(danh_muc.router)
app.include_router(dau_tu.router)
app.include_router(tien_no.router)
app.include_router(tra_no.router)
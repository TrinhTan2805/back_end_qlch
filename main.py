from fastapi import FastAPI
from database.database import engine
from models.base import Base
from app.routers import router_giao_dich as giao_dich
from app.routers import router_thu_nhap as thu_nhap
from app.routers import router_tiet_kiem as tiet_kiem
from app.routers import router_tong_hop as tong_hop
from app.routers import router_danh_muc as danh_muc




app = FastAPI()

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

# Đăng ký router
app.include_router(giao_dich.router)
app.include_router(thu_nhap.router)
app.include_router(tiet_kiem.router)
app.include_router(tong_hop.router)
print("Đăng ký router danh_muc")
app.include_router(danh_muc.router)
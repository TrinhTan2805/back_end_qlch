from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import models_danh_muc
from schemas import schemas_danh_muc

def create_danh_muc(db: Session, danh_muc: schemas_danh_muc.DanhMucCreate):
    db_item = models_danh_muc.DanhMuc(**danh_muc.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_danh_mucs(db: Session):
    return db.query(models_danh_muc).order_by(desc(models_danh_muc.DanhMuc.ngay_nhap)).all()

def get_danh_muc(db: Session, id: int):
    return db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()

def update_danh_muc(db: Session, id: int, danh_muc: schemas_danh_muc.DanhMucUpdate):
    # 1. Tìm Danh mục theo ID
    db_item = db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()

    # 2. Nếu không tìm thấy thì trả về lỗi 404
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Danh mục id={id} không tồn tại"
        )

    # 3. Chuẩn bị dữ liệu cập nhật
    update_data = danh_muc.dict(exclude_unset=True)

    # 4. Nếu 'ngay_nhap' là chuỗi → chuyển thành datetime
    if 'ngay_nhap' in update_data and isinstance(update_data['ngay_nhap'], str):
        try:
            update_data['ngay_nhap'] = datetime.fromisoformat(update_data['ngay_nhap'])
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Định dạng ngày không hợp lệ. Định dạng yêu cầu: YYYY-MM-DD"
            )

    # 5. Cập nhật thuộc tính
    for key, value in update_data.items():
        setattr(db_item, key, value)

    # 6. Lưu thay đổi
    db.commit()
    db.refresh(db_item)

    return db_item

def delete_danh_muc(db: Session, id: int):
    db_item = db.query(models_danh_muc.DanhMuc).filter(models_danh_muc.DanhMuc.id == id).first()
    if not db_item:
        return None
    try:
        db.delete(db_item)
        db.commit()
        return db_item
    except Exception as e:
        db.rollback()
        raise e  # để FastAPI xử lý hoặc bạn có thể raise HTTPException rõ ràng hơn


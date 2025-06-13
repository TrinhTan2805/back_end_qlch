from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import models_giao_dich
from schemas import schemas_giao_dich

def create_giao_dich(db: Session, giao_dich: schemas_giao_dich.GiaoDichCreate):
    db_item = models_giao_dich.GiaoDich(**giao_dich.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_giao_dichs(db: Session):
    return db.query(models_giao_dich.GiaoDich).order_by(desc(models_giao_dich.GiaoDich.ngay_nhap)).all()

def get_giao_dich(db: Session, id: int):
    return db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich.id == id).first()

def update_giao_dich(db: Session, id: int, giao_dich: schemas_giao_dich.GiaoDichUpdate):
    # 1. Tìm giao dịch theo ID
    db_item = db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich.id == id).first()

    # 2. Nếu không tìm thấy thì trả về lỗi 404
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Giao dịch id={id} không tồn tại"
        )

    # 3. Chuẩn bị dữ liệu cập nhật
    update_data = giao_dich.dict(exclude_unset=True)

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

def delete_giao_dich(db: Session, id: int):
    db_item = db.query(models_giao_dich.GiaoDich).filter(models_giao_dich.GiaoDich.id == id).first()
    if not db_item:
        return None
    try:
        db.delete(db_item)
        db.commit()
        return db_item
    except Exception as e:
        db.rollback()
        raise e  # để FastAPI xử lý hoặc bạn có thể raise HTTPException rõ ràng hơn


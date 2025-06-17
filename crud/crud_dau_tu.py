from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import models_dau_tu
from schemas import schemas_dau_tu

def create_dau_tu(db: Session, dau_tu: schemas_dau_tu.DauTuCreate):
    db_item = models_dau_tu.DauTu(**dau_tu.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_dau_tus(db: Session):
    return db.query(models_dau_tu.DauTu).order_by(desc(models_dau_tu.DauTu.ngay_nhap)).all()

def get_dau_tu(db: Session, id: int):
    return db.query(models_dau_tu.DauTu).filter(models_dau_tu.DauTu.id == id).first()

def update_dau_tu(db: Session, id: int, dau_tu: schemas_dau_tu.DauTuUpdate):
    # 1. Tìm giao dịch theo ID
    db_item = db.query(models_dau_tu.DauTu).filter(models_dau_tu.DauTu.id == id).first()

    # 2. Nếu không tìm thấy thì trả về lỗi 404
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Giao dịch id={id} không tồn tại"
        )

    # 3. Chuẩn bị dữ liệu cập nhật
    update_data = dau_tu.dict(exclude_unset=True)

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

def delete_dau_tu(db: Session, id: int):
    db_item = db.query(models_dau_tu.DauTu).filter(models_dau_tu.DauTu.id == id).first()
    if not db_item:
        return None
    try:
        db.delete(db_item)
        db.commit()
        return db_item
    except Exception as e:
        db.rollback()
        raise e  # để FastAPI xử lý hoặc bạn có thể raise HTTPException rõ ràng hơn


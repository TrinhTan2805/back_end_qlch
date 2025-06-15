from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_danh_muc
from schemas import schemas_danh_muc
from database import database

router = APIRouter(prefix="/danh_muc", tags=["danh_muc"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_danh_muc.DanhMucResponse)
def create(danh_muc: schemas_danh_muc.DanhMucCreate, db: Session = Depends(get_db)):
    return crud_danh_muc.create_danh_muc(db, danh_muc)

@router.get("/", response_model=list[schemas_danh_muc.DanhMucResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_danh_muc.get_danh_mucs(db)

@router.get("/{id}", response_model=schemas_danh_muc.DanhMucResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_danh_muc.get_danh_muc(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Danh mục không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_danh_muc.DanhMucResponse)
def update(id: int, danh_muc: schemas_danh_muc.DanhMucUpdate, db: Session = Depends(get_db)):
    db_item = crud_danh_muc.update_danh_muc(db, id, danh_muc)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy Danh mục")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_danh_muc.delete_danh_muc(db, id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Không tìm thấy Danh mục")
        return {"message": "Xóa thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi server khi xóa: {str(e)}")


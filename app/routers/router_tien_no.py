from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_tien_no
from schemas import schemas_tien_no
from database import database

router = APIRouter(prefix="/tien_no", tags=["tien_no"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_tien_no.TienNoResponse)
def create(tien_no: schemas_tien_no.TienNoCreate, db: Session = Depends(get_db)):
    return crud_tien_no.create_tien_no(db, tien_no)

@router.get("/", response_model=list[schemas_tien_no.TienNoResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_tien_no.get_tien_nos(db)

@router.get("/{id}", response_model=schemas_tien_no.TienNoResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_tien_no.get_tien_no(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Tiền nợ không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_tien_no.TienNoResponse)
def update(id: int, tien_no: schemas_tien_no.TienNoUpdate, db: Session = Depends(get_db)):
    db_item = crud_tien_no.update_tien_no(db, id, tien_no)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy Tiền nợ")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_tien_no.delete_tien_no(db, id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Không tìm thấy Tiền nợ")
        return {"message": "Xóa thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi server khi xóa: {str(e)}")


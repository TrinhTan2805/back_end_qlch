from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_dau_tu
from schemas import schemas_dau_tu
from database import database

router = APIRouter(prefix="/dau_tu", tags=["dau_tu"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_dau_tu.DauTuResponse)
def create(dau_tu: schemas_dau_tu.DauTuCreate, db: Session = Depends(get_db)):
    return crud_dau_tu.create_dau_tu(db, dau_tu)

@router.get("/", response_model=list[schemas_dau_tu.DauTuResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_dau_tu.get_dau_tus(db)

@router.get("/{id}", response_model=schemas_dau_tu.DauTuResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    db_item = crud_dau_tu.get_dau_tu(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Giao dịch không tồn tại")
    return db_item

@router.put("/{id}", response_model=schemas_dau_tu.DauTuResponse)
def update(id: int, dau_tu: schemas_dau_tu.DauTuUpdate, db: Session = Depends(get_db)):
    db_item = crud_dau_tu.update_dau_tu(db, id, dau_tu)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
    return db_item

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_dau_tu.delete_dau_tu(db, id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch")
        return {"message": "Xóa thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi server khi xóa: {str(e)}")


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import database
models.Base.metadata.create_all(bind=database.engine)
app=FastAPI()
def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notes/",response_model=schemas.NoteResponse)
async def create_note(note:schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@app.get("/notes/{note_id}",response_model=schemas.NoteResponse)
async def read_note(note_id:int, db: Session =Depends(get_db)):
    note= db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}",response_model=schemas.NoteResponse)
async def update_note(note_id:int, note: schemas.NoteCreate ,db: Session =Depends(get_db)):
    db_note=db.query(models.Note).filter(models.Note.id==note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db_note.title=note.title
    db_note.content=note.content
    db.commit()
    db.refresh(db_note)
    return db_note

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int, db: Session=Depends(get_db)):
    note=db.query(models.Note).filter(models.Note.id==note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"detail":"Note deleted"}
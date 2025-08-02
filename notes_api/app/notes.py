from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List,Optional
from .. import crud,schemas,database
router = APIRouter(prefix="api/notes",tags=["notes"])

@router.get("/", response_model=List[schemas.Note])
def read_notes(
    skip: int =0,
    limit: int=10,
    search: Optional[str] = None,
    category: Optional[str] =None,
    is_favourite: Optional[bool]=None,
    is_archived: Optional[bool]=None,
    sort_by: str= Query("created at", regex="^(created_at|updated_at|title)$"),
    sort_order: str= Query("desc", regex="^(asc|desc)$"),
    db: Session = Depends(database.get_db) 
):
    notes=crud.get_notes(db,skip=skip,limit=limit, search=search,category=category,is_favourite=is_favourite, is_archived=is_archived,sort_by=sort_by,sort_order=sort_order)
    return notes

@router.get("/{note_id}", response_model=schemas.Note)
def read_note(note_id: int,db:Session = Depends(database.get_db)):
    note= crud.get_note(db, note_id=note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=schemas.Note)
def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
   db: Session= Depends(database.get_db)
):
    update_note =crud.update_note(db, note_id=note_id, note=note)
    if update_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return update_note

@router.get("/categories/list")
def get_categories(db: Session = Depends(database.get_db)):
    categories = crud.get_categories(db)
    return [cat[0]for cat in categories if cat[0]]

@router.delete("/{note_id}")
def delete_note(note_id:int,db: Session = Depends(database.get_db)):
    note= crud.delete_note(db, note_id=note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted successfully"}
from sqlalchemy.orm import Session
from sqlalchemy import or_, asc, desc
from . import models, schemas
from typing import Optional

def get_notes(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        category: str = None,
        is_favorite: Optional[bool] = None,
        is_archived: Optional[bool] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"):
    query= db.query(models.Note)
    if search:
        query=query.filter(
            or_(
                models.Note.title.contains(search),
                models.Note.content.contains(search),
                models.Note.tags.contains(search)
            )
        )
        if category:
            query = query.filter(models.Note.category == category)
        if is_favorite is not None:
            query = query.filter(models.Note.is_favorite == is_favorite)
        if is_archived is not None:
            query = query.filter(models.Note.is_archived == is_archived)

        if sort_order== "desc":
            query=query.order_by(desc(getattr(models.Notes, sort_by)))
        else:
            query=query.order_by(asc(getattr(models.Note, sort_by)))
        return query.offset(skip).limit(limit).all()

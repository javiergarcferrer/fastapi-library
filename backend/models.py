from typing import Optional

from pydantic import BaseModel

from datetime import date

class Book(BaseModel):
    name: str
    author: str
    description: Optional[str] = None
    isbn: Optional[str] = None
    status: Optional[int] = None

class Author(BaseModel):
    name: str
    birth_date: Optional[date] = None
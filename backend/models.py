from typing import Optional

from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author: str
    description: Optional[str] = None
    status: Optional[int] = None
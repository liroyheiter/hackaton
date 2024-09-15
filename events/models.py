from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    id: int
    title: str
    description: str
    category: str
    chat_link: Optional[str] = None
    image_url: Optional[str] = None

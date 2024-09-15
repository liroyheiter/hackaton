from pydantic import BaseModel
from typing import Optional

class Ad(BaseModel):
    id: int
    description: str
    phone_number: str
    image_url: Optional[str] = None

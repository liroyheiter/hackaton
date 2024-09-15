from pydantic import BaseModel

class EventCreate(BaseModel):
    photo: str
    description: str
    chat_link: str
    category: str

class EventOut(EventCreate):
    event_id: int

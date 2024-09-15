from pydantic import BaseModel

class AdCreate(BaseModel):
    photo: str
    description: str
    phone_number: str

class AdOut(AdCreate):
    ad_id: int

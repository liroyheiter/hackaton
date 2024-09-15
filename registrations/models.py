from pydantic import BaseModel

class Registrations(BaseModel):
    user_id: str
    event_id: str

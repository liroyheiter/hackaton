from pydantic import BaseModel

class RegistrationCreate(BaseModel):
    user_id: int
    event_id: int

class RegistrationOut(RegistrationCreate):
    pass

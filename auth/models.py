from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username: str
    password: str
    registered_events: List[int] = []  # Список ID ивентов, на которые зарегистрирован пользователь

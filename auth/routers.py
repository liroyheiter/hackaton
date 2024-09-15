from fastapi import APIRouter, HTTPException
from typing import List
from .models import User

router = APIRouter()

# Локальное хранилище данных для пользователей
users = []

@router.post("/register/", response_model=User)
async def register_user(user: User):
    if any(u.username == user.username for u in users):
        raise HTTPException(status_code=400, detail="Username already taken")
    users.append(user)
    return user

@router.get("/users/{user_id}/events-count")
async def get_user_events_count(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "events_registered": len(user.registered_events)}

@router.post("/users/{user_id}/register-event/{event_id}")
async def register_for_event(user_id: int, event_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if event_id in user.registered_events:
        raise HTTPException(status_code=400, detail="Already registered for this event")
    user.registered_events.append(event_id)
    return {"message": f"User {user.username} successfully registered for event {event_id}"}

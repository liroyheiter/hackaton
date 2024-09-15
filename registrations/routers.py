from fastapi import APIRouter, HTTPException
from registrations.models import Registrations
from registrations.schemas import RegistrationCreate, RegistrationOut
from database import registrations_collection
from bson import ObjectId

router = APIRouter()

# Зарегистрироваться на событие
@router.post("/", response_model=RegistrationOut)
async def register_for_event(registration: RegistrationCreate):
    existing_reg = await registrations_collection.find_one({
        "user_id": ObjectId(registration.user_id),
        "event_id": ObjectId(registration.event_id)
    })
    
    if existing_reg:
        raise HTTPException(status_code=400, detail="User already registered for this event")
    
    new_registration = registration.dict()
    await registrations_collection.insert_one(new_registration)

    return new_registration

from fastapi import APIRouter, HTTPException
from typing import List
from .models import Event

router = APIRouter()

# Локальное хранилище данных для событий
events = []

@router.get("/", response_model=List[Event])
async def get_events():
    return events

@router.post("/", response_model=Event)
async def create_event(event: Event):
    events.append(event)
    return event

@router.get("/{event_id}", response_model=Event)
async def get_event(event_id: int):
    event = next((event for event in events if event.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.get("/filter/{category}", response_model=List[Event])
async def filter_events_by_category(category: str):
    filtered_events = [event for event in events if event.category == category]
    return filtered_events

from fastapi import FastAPI
from events.routers import router as event_router
from ads.routers import router as ad_router
from auth.routers import router as auth_router

app = FastAPI()

# Подключаем маршруты
app.include_router(event_router, prefix="/events", tags=["events"])
app.include_router(ad_router, prefix="/ads", tags=["ads"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

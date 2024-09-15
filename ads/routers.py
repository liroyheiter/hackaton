from fastapi import APIRouter, HTTPException
from typing import List
from .models import Ad

router = APIRouter()

# Локальное хранилище данных для объявлений
ads = []

@router.get("/", response_model=List[Ad])
async def get_ads():
    return ads

@router.post("/", response_model=Ad)
async def create_ad(ad: Ad):
    ads.append(ad)
    return ad

@router.get("/{ad_id}", response_model=Ad)
async def get_ad(ad_id: int):
    ad = next((ad for ad in ads if ad.id == ad_id), None)
    if ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad

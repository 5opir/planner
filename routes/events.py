from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await Event.find_all().to_list()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await Event.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="События с таким ИД не существует"
        )
    return event

@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await body.create()
    return {"message": "Событие создано"}

@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    event = await Event.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="События с таким ИД не существует"
        )

    # Обновляем только переданные поля
    update_data = body.dict(exclude_unset=True)
    update_query = {"$set": update_data}
    await event.update(update_query)
    return await Event.get(id)

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await Event.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="События с таким ИД не существует"
        )

    await event.delete()
    return {"message": "Событие удалено"}
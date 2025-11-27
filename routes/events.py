from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
import json
from database.connection import get_session
from models.events import Event, EventCreate, EventUpdate

event_router = APIRouter(tags=["Events"])

@event_router.post("/new")
async def create_event(new_event: EventCreate, session: Session = Depends(get_session)):
    # Конвертируем tags в JSON строку
    event_data = new_event.dict()
    event_data['tags'] = json.dumps(new_event.tags)
    
    db_event = Event(**event_data)
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    
    return {"message": "СОБЫТИЕ СОЗДАНО УСПЕШНО"}

@event_router.get("/", response_model=list[Event])
async def retrieve_all_events(session: Session = Depends(get_session)):
    events = session.exec(select(Event)).all()
    
    # Конвертируем tags обратно в список
    for event in events:
        event.tags = json.loads(event.tags)
    
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="СОБЫТИЕ С ТАКИМ ИД НЕ НАЙДЕНО"
        )
    
    event.tags = json.loads(event.tags)
    return event

@event_router.put("/{id}")
async def update_event(id: int, event_data: EventUpdate, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="СОБЫТИЕ С ТАКИМ ИД НЕ НАЙДЕНО"
        )
    
    # Обновляем только переданные поля
    update_data = event_data.dict(exclude_unset=True)
    
    # Если обновляются tags, конвертируем в JSON
    if 'tags' in update_data:
        update_data['tags'] = json.dumps(update_data['tags'])
    
    for field, value in update_data.items():
        setattr(event, field, value)
    
    session.add(event)
    session.commit()
    session.refresh(event)
    
    event.tags = json.loads(event.tags)
    return {"message": "СОБЫТИЕ ОБНОВЛЕНО УСПЕШНО"}

@event_router.delete("/{id}")
async def delete_event(id: int, session: Session = Depends(get_session)):
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="СОБЫТИЕ С ТАКИМ ИД НЕ НАЙДЕНО"
        )
    
    session.delete(event)
    session.commit()
    return {"message": "СОБЫТИЕ УДАЛЕНО УСПЕШНО"}
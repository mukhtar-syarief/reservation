from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import BaseModel

from ..models.invoices_guests import InvoiceGuestResponse
from ..database import Session, get_db
from ..models.reservations import Reservations
from ..user.auth import TokenData, get_token_data



router = APIRouter(tags= ['Reservation API'])


class ReservationsResponse(BaseModel):
    id: int
    guest_id: int
    start_time: datetime
    end_time: datetime
    create_at: datetime
    last_change: datetime
    discount_percent: float
    total_price: int


@router.get('', response_model=Page[ReservationsResponse])
async def get_guest_reservation(
    guest_data: TokenData = Depends(get_token_data),
    db: Session = Depends(get_db),
    params: Params = Depends()):

    reservations = db.query(Reservations).filter(Reservations.guest_id == guest_data.id)
    return paginate(reservations, params)


@router.post('', response_model=InvoiceGuestResponse)
async def create_reservation(
    payload,
    db: Session = Depends(get_db)):
    raise NotImplementedError


@router.get('/{reservation_id}')
async def get_reservation():
    raise NotImplementedError


@router.put('/{reservation_id}')
async def cancel_reservation():
    raise NotImplementedError
    

@router.put('/{reservation_id}')
async def change_reservation():
    raise NotImplementedError
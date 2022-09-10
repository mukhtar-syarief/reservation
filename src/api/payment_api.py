from fastapi import APIRouter

from ..database import Session, get_db


router= APIRouter(tags= ['Payment API'])



@router.get('')
async def get_guest_payment_info(
    reservation_id: int,
    db: Session = Depends(get_db)
):
    raise NotImplementedError

@router.post('')
async def upload_evidence_payment():
    raise NotImplementedError

@router.put('')
async def verify_payment():
    raise NotImplementedError
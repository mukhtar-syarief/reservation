from fastapi import Depends

from ..models.reservations import Reservations
from ..database import get_db, Session


class ReservationRepo:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db
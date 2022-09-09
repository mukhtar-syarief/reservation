from fastapi import APIRouter, Depends

from ..repos.field_repo import FieldRepo
from ..service.field_service import FieldService, FieldUpdatePayload
from ..database import Session, get_db


router= APIRouter(tags=['Field API'])



@router.get('/{field_id}')
async def get_field_info(
    field_id: int,
    db: Session = Depends(get_db),
    field_repo: FieldRepo = Depends(FieldRepo)):

    return await field_repo.get_field_by_id(field_id)


@router.put('/{field_id}')
async def update_field(
    field_id: int,
    payload: FieldUpdatePayload,
    db: Session = Depends(get_db),
    field_service: FieldService = Depends(FieldService)):

    await field_service.update_field(field_id, payload)

    return {'message': 'success'}


@router.delete('/{field_id}')
async def delete_field():
    raise NotImplementedError
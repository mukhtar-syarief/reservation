from fastapi import APIRouter



router= APIRouter(tags=['Field API'])



@router.get('/{field_id}')
async def get_field_info():
    raise NotImplementedError


@router.put('/{field_id}')
async def update_field():
    raise NotImplementedError


@router.delete('/{field_id}')
async def delete_field():
    raise NotImplementedError
from fastapi import APIRouter



router = APIRouter(tags= ['Training Centre API'])



@router.get('')
async def get_training_centre_info():
    raise NotImplementedError


@router.post('')
async def register_training_centre():
    raise NotImplementedError


@router.put('/{training_centre_id}')
async def edit_training_centre_info():
    raise NotImplementedError
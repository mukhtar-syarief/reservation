import uvicorn
from fastapi import FastAPI

from src.api import login_api
from src.api import field_api
from src.api import reservations_api
from src.api import training_centre_api


app = FastAPI()

app.include_router(login_api.router, prefix= 'reservation/v1/login')
app.include_router(field_api.router, prefix= 'reservation/v2/field')
app.include_router(reservations_api.router, prefix= ' reservation/v2/reservation')
app.include_router(training_centre_api.router, prefix= 'reservation/v2/training_centre')



@app.get('/cek')
def check_status():
    return {'message': 'Oke'}



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
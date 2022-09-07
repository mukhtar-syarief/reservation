from fastapi import FastAPI


app = FastAPI()





@app.get('/cek')
def check_status():
    return {'message': 'Oke'}
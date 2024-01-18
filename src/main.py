from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from databricks.labs.ucx import install

class DBX_param(BaseModel):
    host: str
    token: str


app = FastAPI()

@app.get("/")
async def root():
    return {"FAST API is running"}


@app.post('/ucx_api')
async def start_executing_ucx(dbx_param: DBX_param):
    print(f"host is {dbx_param.host}")
    print(f"tokenis is {dbx_param.token}")
    install.main_install(dbx_param.host, dbx_param.token) 
    return {"message": "Success"}
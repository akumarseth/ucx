from fastapi import FastAPI, Response, Request, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from databricks.labs.ucx import install

class DBX_param(BaseModel):
    host: str
    token: str


async def catch_exceptions_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

def start_application():
    app = FastAPI()
    app.middleware('http')(catch_exceptions_middleware)
    return app

app = start_application()

@app.get("/")
async def root():
    return {"FAST API is running"}


@app.post('/ucx_api')
async def start_executing_ucx(dbx_param: DBX_param, background_tasks: BackgroundTasks):
    print(f"host is {dbx_param.host}")
    print(f"tokenis is {dbx_param.token}")
    
    background_tasks.add_task(install.main_install, dbx_param.host, dbx_param.token)

    # install.main_install(dbx_param.host, dbx_param.token) 
    return {"message": "Success"}
from fastapi import FastAPI

from app.api.incedent_handler import incedent_router


app = FastAPI(
    openapi_url="/api/v1/ucar/openapi.json",
    docs_url="/api/v1/ucar/docs"
)

app.include_router(incedent_router, prefix='/api/v1/incedents', tags=['incedents'])


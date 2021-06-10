from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse
from src.core.utils import treating_data
from src.handlers.consult_property import processing_data


class Property(BaseModel):
    neighborhood: str
    transaction: str


class ResponseProperty(BaseModel):
    n_obs: int
    preco_m2: float
    range: dict


consult_property_router = APIRouter()


@consult_property_router.post("/consult-property/", response_model=ResponseProperty)
async def consult_property(property: Property):
    data = await processing_data(dict(property))
    if data is False:
        return JSONResponse(status_code=500, content={"Detail": "Does not possible consult this information, api external is offline."})
    n_obs, median, area = treating_data(data)
    response = {
        "n_obs": len(data),
        "preco_m2": median,
        "range": area
    }
    return response

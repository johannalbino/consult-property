from fastapi import APIRouter
from pydantic import BaseModel


class Property(BaseModel):
    neighborhood: str
    transaction: str


consult_property_router = APIRouter()


@consult_property_router.post("/consult-property/")
def consult_property(property: Property):
    return property

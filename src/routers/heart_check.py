from fastapi import APIRouter

heart_check_router = APIRouter()


@heart_check_router.get("/heart-check")
async def heart_check():
    return {"Detail": "All OK!"}

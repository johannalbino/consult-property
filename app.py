from fastapi import FastAPI
import uvicorn
from src.handlers import heart_check_router, consult_property_router
from src.core.config import ENVIRONMENT


app = FastAPI(
    title="Viva Não Real",
    docs_url="/docs",
    redoc_url="/redocs"
)


app.include_router(heart_check_router)
app.include_router(consult_property_router)


if __name__ == "__main__":
    uvicorn.run(
        "app:app" if ENVIRONMENT == "dev" else app,
        workers=1,
        reload=True
    )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mangum import Mangum
from src.routers import heart_check_router, consult_property_router
from src.core.config import ENVIRONMENT


app = FastAPI(
    title="Viva Não Real",
    docs_url="/docs",
    redoc_url="/redocs"
)


app.include_router(heart_check_router)
app.include_router(consult_property_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"]
)


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run(
        "app:app" if ENVIRONMENT == "dev" else app,
        workers=2,
        reload=True
    )

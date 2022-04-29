from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from whiterun.config import settings
from whiterun.database import engine
from whiterun.endpoints.payments import router as payments_router
from whiterun.endpoints.webhooks import router as webhooks_router
from whiterun.endpoints.shared import router as shared_router
from whiterun.shared.models import BaseModel

BaseModel.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(webhooks_router, prefix="/webhooks", tags=["Webhooks"])
app.include_router(shared_router, tags=["Shared"])

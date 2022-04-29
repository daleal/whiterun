import uuid

from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from whiterun.constants import RECIPIENT_ACCOUNT
from whiterun.shared.initializers import FINTOC_CLIENT
from whiterun.shared.models import BaseModel


class Payment(BaseModel):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    fintoc_intent_id = Column(String, nullable=False, unique=True, index=True)
    amount = Column(Integer, nullable=False)
    accepted = Column(Boolean, nullable=False, index=True, default=False)

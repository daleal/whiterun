from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import whiterun.crud.payments as payments_crud
import whiterun.schemas.payment as payment_schemas
from whiterun import deps
from whiterun.models.payment import Payment as PaymentModel

router = APIRouter()


@router.post("/intent", response_model=payment_schemas.PaymentCreationResponse)
def create_payment_intent(
    payment: payment_schemas.PaymentCreation,
    db: Session = Depends(deps.get_db),
) -> payment_schemas.PaymentCreationResponse:
    widget_token = payments_crud.create(db, payment)
    return payment_schemas.PaymentCreationResponse(widget_token=widget_token)


@router.get("/accepted", response_model=List[payment_schemas.PaymentResponse])
def list_accepted_payments(db: Session = Depends(deps.get_db)) -> List[PaymentModel]:
    return payments_crud.list_accepted(db)

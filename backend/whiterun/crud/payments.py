from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from whiterun.constants import CURRENCY, RECIPIENT_ACCOUNT
from whiterun.models.payment import Payment as PaymentModel
from whiterun.schemas.payment import (
    PaymentCreation as PaymentCreationSchema,
    PaymentUpdate as PaymentUpdateSchema,
)
from whiterun.shared.initializers import FINTOC_CLIENT


def get_by_fintoc_id(db: Session, fintoc_id: str, silent: bool = False) -> PaymentModel:
    payment = db.query(PaymentModel).filter(
        PaymentModel.fintoc_intent_id == fintoc_id,
    ).first()
    if not silent and not payment:
        raise HTTPException(
            status_code=404,
            detail=f"No payment intent with Fintoc id {fintoc_id}",
        )
    return payment


def list_accepted(db: Session) -> List[PaymentModel]:
    return list(db.query(PaymentModel).filter(
        PaymentModel.accepted == True  # noqa: E712
    ))


def create(db: Session, payment_schema: PaymentCreationSchema) -> str:
    payment_intent = FINTOC_CLIENT.payment_intents.create(
        currency=CURRENCY,
        amount=payment_schema.amount,
        recipient_account=RECIPIENT_ACCOUNT,
    )
    payment = PaymentModel(
        fintoc_intent_id=payment_intent.id,
        amount=payment_schema.amount,
        accepted=False,
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment_intent.widget_token


def update(
    db: Session,
    payment_schema: PaymentUpdateSchema,
    payment: PaymentModel,
) -> PaymentModel:
    for key, value in payment_schema.dict(exclude_unset=True).items():
        setattr(payment, key, value)
    db.commit()
    db.refresh(payment)
    return payment

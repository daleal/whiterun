from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

import whiterun.crud.payments as payments_crud
import whiterun.schemas.payment as payment_schemas
from whiterun import deps
from whiterun.middleware.webhooks import (
    require_signature_validation,
    require_timestamp_validation,
)
from whiterun.models.payment import Payment as PaymentModel

router = APIRouter()


@router.post(
    "/payments/accepted",
    dependencies=[
        # Depends(require_timestamp_validation),
        # Depends(require_signature_validation),
    ],
)
def accept_payment_webhook(
    content: payment_schemas.PaymentAcceptedWebhook,
    db: Session = Depends(deps.get_db),
) -> Response:
    payment = payments_crud.get_by_fintoc_id(db, content.data.id)
    update_schema = payment_schemas.PaymentUpdate(accepted=True)
    payments_crud.update(db, update_schema, payment)
    return Response(status_code=200)

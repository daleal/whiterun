from datetime import datetime
from typing import List, Optional

from pydantic import Extra, UUID4, StrictBool, StrictInt, StrictStr

from whiterun.shared.schemas import BaseSchema


class PaymentCreation(BaseSchema):
    amount: StrictInt


class PaymentUpdate(BaseSchema):
    accepted: StrictBool


class PaymentCreationResponse(BaseSchema):
    widget_token: StrictStr


class PaymentResponse(BaseSchema):
    id: UUID4
    amount: StrictInt
    fintoc_intent_id: StrictStr
    accepted: StrictBool
    updated_at: datetime


# Webhook
class BaseWebhookSchema(BaseSchema):
    class Config:
        extra = Extra.ignore


class PaymentAcceptedWebhookDataAccount(BaseWebhookSchema):
    type: StrictStr
    number: StrictStr
    holder_id: StrictStr
    institution_id: StrictStr


class PaymentAcceptedWebhookData(BaseWebhookSchema):
    id: StrictStr
    mode: StrictStr
    amount: StrictInt
    status: StrictStr
    currency: StrictStr
    sender_account: Optional[PaymentAcceptedWebhookDataAccount] = None
    recipient_account: Optional[PaymentAcceptedWebhookDataAccount] = None


class PaymentAcceptedWebhook(BaseWebhookSchema):
    id: StrictStr
    type: StrictStr
    mode: StrictStr
    data: PaymentAcceptedWebhookData

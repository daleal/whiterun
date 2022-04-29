import hmac
from hashlib import sha256
from typing import List

from fastapi import HTTPException, Request

from whiterun.config import settings
from whiterun.utils import now_timestamp


def process_signature(request: Request, header_name: str) -> List[str]:
    fintoc_signature_header = request.headers.get(header_name)

    if fintoc_signature_header is None:
        raise HTTPException(status_code=400, detail="Missing signature")

    return [x.split("=")[1] for x in fintoc_signature_header.split(",")]


async def form_message(request: Request, timestamp: str) -> str:
    request_body = (await request.body()).decode('utf-8')
    return f"{timestamp}.{request_body}"


def generate_signature(secret: str, message: str) -> str:
    encoded_secret = secret.encode('utf-8')
    encoded_message = message.encode('utf-8')
    hmac_object = hmac.new(encoded_secret, msg=encoded_message, digestmod=sha256)
    return hmac_object.hexdigest()


def compare_signatures(local: str, event: str) -> bool:
    return hmac.compare_digest(local, event)


async def require_signature_validation(request: Request) -> None:
    timestamp, event_signature = process_signature(request, 'Fintoc-Signature')
    message = await form_message(request, timestamp)

    signature = generate_signature(settings.fintoc_webhook_secret, message)

    if not compare_signatures(signature, event_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")


async def require_timestamp_validation(request: Request) -> None:
    timestamp, _ = process_signature(request, 'Fintoc-Signature')
    if int(timestamp) + settings.webhook_tolerance_seconds < now_timestamp():
        raise HTTPException(status_code=400, detail="Invalid timestamp")

import uuid
from yookassa import Configuration, Payment

YOOKASSA_SHOP_ID = "1031381"
YOOKASSA_SECRET_KEY = "test_5Qi9jsaJKdXI5-Q56sVkMlOUBcp2Ah-yomwlIFTDkFY"

Configuration.account_id = YOOKASSA_SHOP_ID
Configuration.secret_key = YOOKASSA_SECRET_KEY


def create_payment(amount, return_url):
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": return_url
        },
        "capture": True,
        "description": f"Оплата заказа {uuid.uuid4()}"
    })

    return payment.confirmation.confirmation_url if payment.confirmation else None

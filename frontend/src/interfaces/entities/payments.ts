import type { DateTime } from 'luxon';

export interface PaymentIntent {
  widgetToken: string
}

interface BasePayment {
  id: string
  amount: number
  fintocIntentId: string
  accepted: boolean
}

export interface APIPayment extends BasePayment {
  updatedAt: string
}

export interface Payment extends BasePayment {
  updatedAt: DateTime
}

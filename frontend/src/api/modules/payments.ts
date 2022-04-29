import client from '@/api/client';
import { PaymentIntent, APIPayment } from '@/interfaces/entities/payments';

export const listAccepted = async (): Promise<Array<APIPayment>> => {
  const response = await client.get('/payments/accepted');
  return response.data;
};

export const create = async (amount: number): Promise<PaymentIntent> => {
  const response = await client.post('/payments/intents', { amount });
  return response.data;
};

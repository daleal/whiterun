import type { DateTime } from 'luxon';

export const formatDateTime = (dateTime: DateTime) => dateTime.toFormat('HH:mm:ss - dd/LL/yyyy');

export const formatMoney = (money: number) => money.toLocaleString('es-CL');

export const cleanNumber = (possibleNumber: string) => {
  if (!possibleNumber) {
    return '';
  }

  return possibleNumber.replace(/[^0-9]/g, '');
};

export const isValidNumber = (possibleNumber: string) => (
  possibleNumber === cleanNumber(possibleNumber)
);

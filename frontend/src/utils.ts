import type { DateTime } from 'luxon';

export const formatDateTime = (dateTime: DateTime) => dateTime.toFormat('HH:mm:ss - dd/LL/yyyy');

export const formatMoney = (money: number) => money.toLocaleString('es-CL');

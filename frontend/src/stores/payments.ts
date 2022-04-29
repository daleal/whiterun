import { defineStore, acceptHMRUpdate } from 'pinia';
import { DateTime } from 'luxon';
import * as api from '@/api';
import { Payment } from '@/interfaces/entities/payments';

export const usePaymentsStore = defineStore('payments', {
  state: () => ({
    loading: false,
    acceptedPayments: <Array<Payment>>[],
  }),
  actions: {
    async loadAcceptedPayments() {
      this.loading = true;
      const rawPayments = await api.payments.listAccepted();

      const payments = rawPayments.map((payment) => ({
        ...payment,
        updatedAt: DateTime.fromISO(`${payment.updatedAt}Z`),
      }));
      payments.sort((a, b) => b.updatedAt.toMillis() - a.updatedAt.toMillis());
      this.acceptedPayments = payments;
      this.loading = false;
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(usePaymentsStore, import.meta.hot));
}

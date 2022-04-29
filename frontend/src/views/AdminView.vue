<script setup lang="ts">
import { onMounted } from 'vue';
import { usePaymentsStore } from '@/stores/payments';
import PaymentCard from '@/components/PaymentCard.vue';
import ReloadButton from '@/components/ReloadButton.vue';

const paymentsStore = usePaymentsStore();

const load = () => {
  paymentsStore.loadAcceptedPayments();
};

onMounted(load);
</script>

<template>
  <v-container class="mt-2 pb-16">
    <PaymentCard
      v-for="payment in paymentsStore.acceptedPayments"
      :key="payment.fintocIntentId"
      :payment="payment"
      class="mb-4"
    />
  </v-container>
  <ReloadButton
    :loading="paymentsStore.loading"
    @reload="load"
  />
</template>

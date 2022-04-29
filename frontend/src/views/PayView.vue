<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { usePaymentsStore } from '@/stores/payments';
import { useFintocWidget } from '@/composables/fintocWidget';
import { cleanNumber, isValidNumber } from '@/utils';

const paymentsStore = usePaymentsStore();
const route = useRoute();

const paying = ref(false);
const amount = ref('');

const input = (event: Event) => {
  amount.value = cleanNumber((event.target as HTMLInputElement)?.value);
};

const setPaying = (value: boolean) => {
  paying.value = value;
};

const pay = async () => {
  setPaying(true);

  const paymentIntent = await paymentsStore.createPaymentIntent(Number(amount.value));

  const widget = await useFintocWidget({
    widgetToken: paymentIntent.widgetToken,
    onSuccess: () => setPaying(false),
    onExit: () => setPaying(false),
  });

  if (widget) {
    widget.open();
  } else {
    setPaying(false);
  }
};

onMounted(() => {
  const routeAmount = route.params.amount as string;

  if (isValidNumber(routeAmount)) {
    amount.value = routeAmount;
    pay();
  }
});
</script>

<template>
  <v-container class="h-100 d-flex flex-column justify-end">
    <v-form class="mb-3">
      <v-text-field
        v-model="amount"
        label="Amount"
        variant="outlined"
        class="mb-4"
        :disabled="paying"
        hide-details
        @input="input"
      />
      <div class="w-100 d-flex justify-end">
        <v-btn
          size="large"
          :disabled="paying"
          @click="pay"
        >
          Pay!
        </v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<style scoped>
.h-100 {
  height: 100%;
}

.w-100 {
  width: 100%;
}
</style>

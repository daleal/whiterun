<script setup lang="ts">
import { formatDateTime, formatMoney } from '@/utils';
import type { Payment } from '@/interfaces/entities/payments';

const props = defineProps<{ payment: Payment }>();
</script>

<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div>
        Payment for
      </div>
      <p class="mt-2 text-h3">
        $ {{ formatMoney(props.payment.amount) }}
      </p>
      <p class="mt-1 text-h6">
        {{ formatDateTime(props.payment.updatedAt) }}
      </p>
    </v-card-text>
  </v-card>
</template>

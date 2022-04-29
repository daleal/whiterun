<script setup lang="ts">
import { formatDateTime, formatMoney } from '@/utils';
import type { Payment } from '@/interfaces/entities/payments';

const props = defineProps<{ payment: Payment }>();
</script>

<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div class="mb-1">
        Payment for
      </div>
      <p class="text-h3">
        $ {{ formatMoney(props.payment.amount) }}
      </p>
      <p class="mt-1">
        {{ formatDateTime(props.payment.updatedAt) }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { cleanNumber } from '@/utils';

const amount = ref('');

const input = (event: Event) => {
  amount.value = cleanNumber((event.target as HTMLInputElement)?.value);
};

const pay = () => {
  console.log('Payin\'...');
};
</script>

<template>
  <v-container class="h-100 d-flex flex-column justify-end">
    <v-form class="mb-3">
      <v-text-field
        v-model="amount"
        label="Amount"
        variant="outlined"
        class="mb-4"
        hide-details
        @input="input"
      />
      <div class="w-100 d-flex justify-end">
        <v-btn
          size="large"
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

<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';
import { POLLING_INTERVAL_IN_SECONDS } from '@/constants';
import * as api from '@/api';
import { Nullable } from '@/interfaces/common';

let interval: Nullable<number> = null;

onMounted(() => {
  interval = setInterval(() => {
    api.common.healthCheck();
  }, POLLING_INTERVAL_IN_SECONDS * 1000);
});

onUnmounted(() => {
  if (interval !== null) {
    clearInterval(interval);
  }
});
</script>

<template>
  <v-app class="height-full overflow-auto">
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<style scoped>
.height-full {
  height: 100vh;
}
</style>

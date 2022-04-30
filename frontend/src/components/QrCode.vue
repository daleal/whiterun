<script setup lang="ts">
import QrcodeVue from 'qrcode.vue';

const props = defineProps<{ url: string }>();
</script>

<template>
  <div>
    <QrcodeVue
      :value="props.url"
      :size="1000"
      render-as="svg"
      class="h-100 w-100"
    />
  </div>
</template>

<style scoped>
.h-100 {
  height: 100%;
}

.w-100 {
  width: 100%;
}
</style>

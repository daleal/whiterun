<script setup lang="ts">
const props = defineProps<{ loading: boolean }>();

const emit = defineEmits<{ (e: 'reload'): void }>();

const reload = () => {
  emit('reload');
};
</script>

<template>
  <v-btn
    class="mr-4 mb-4"
    :class="{ spin: props.loading }"
    icon="mdi-cached"
    color="secondary"
    elevation="24"
    position="fixed"
    size="x-large"
    :disabled="props.loading"
    bottom
    right
    @click="reload"
  />
</template>

<style scoped>
.spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>

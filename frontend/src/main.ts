import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import App from '@/App.vue';
import router from '@/router';

import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css';
import '@/assets/styles/base.css';

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'dark',
  },
});

const app = createApp(App);

app.use(createPinia());
app.use(vuetify);
app.use(router);

app.mount('#app');

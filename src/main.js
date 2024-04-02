import './assets/base.css'

import { createApp } from 'vue'
import { RouterLink } from 'vue-router';
import PrimeVue from 'primevue/config';
import App from './App.vue'
// import { Plotly } from "/node_modules/vue-plotly/src/index.js";

import "primevue/resources/themes/lara-light-indigo/theme.css";
import '/node_modules/primeflex/primeflex.css'   
import '/node_modules/primeicons/primeicons.css';
// <script src= charset="utf-8"></script>

const app = createApp(App);

app.use(PrimeVue);
app.component('router-link', RouterLink);
app.mount('#app')

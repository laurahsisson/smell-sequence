<script setup>
import { ref } from 'vue'
import { CardState } from '@/constants.js'

import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';

defineEmits(['select-card'])
const props = defineProps(['boxes', 'states'])

const hide = ref(false);

function severity(state) {
    switch (state) {
        case CardState.Selected:
            return "info";
        case CardState.Highlighted:
            return "success";
        case CardState.Danger:
            return "danger";
        default:
            return "secondary";
    }
}
</script>
<template>
    <div class="mb-2">
        <Checkbox v-model="hide" inputId="hideLabel" :binary="true" />
        <label for="hideLabel" class="ml-2"> Hide labels? </label>
    </div>
    <div class="grid">
        <div class="col-3" v-for="(box,i) in boxes">
            <Button outlined :raised="states[box.name].state!=CardState.Default" :disabled="!states[box.name].enabled" :severity="severity(states[box.name].state)" @click="$emit('select-card',box)" class="w-full" :class="{'font-semibold': states[box.name].state!=CardState.Default}" :label="(hide) ? 'Box ' + (i+1) : box.name" />
        </div>
    </div>
</template>
<style scoped>
</style>